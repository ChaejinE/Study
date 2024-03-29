provider "aws" {
  region = "us-west-2"
}

resource "aws_key_pair" "web" {
  public_key = file("/Users/reconlabs/.ssh/id_rsa.pub")
}

resource "aws_security_group" "ssh-access" {
  name = "ssh-access"
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group" "nginx-access" {
  name = "nginx_access"
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port        = 0
    to_port          = 0
    protocol         = "-1"
    cidr_blocks      = ["0.0.0.0/0"]
    ipv6_cidr_blocks = ["::/0"]
  }
}

output "publicip" {
  value = aws_instance.web.public_ip
}

resource "aws_instance" "web" {
  ami           = "ami-0ab193018f3e9351b"
  instance_type = "t2.micro"

  tags = {
    name = "web server"
  }

  key_name = aws_key_pair.web.id

  # for aws_instance only
  # azure: custom_data
  # gcp: meta_data
#   user_data = <<-EOF
#     #! /bin/bash
#     sudo yum update
#     sudo yum install nginx -y
#     sudo service nginx start
#     sudo chkconfig nginx on
#     sudo service nginx status
#   EOF

  provisioner "remote-exec" {
    inline = [
      "sudo yum update",
      "sudo yum install nginx -y",
      "sudo service nginx start",
      "sudo chkconfig nginx on"
    ]
  }

  connection {
    type        = "ssh"
    host        = self.public_ip
    user        = "ec2-user"
    private_key = file("/Users/reconlabs/.ssh/id_rsa")
  }

  provisioner "local-exec" {
    on_failure = fail
    command    = "echo ${aws_instance.web.public_ip} >> /tmp/public_ip.txt"
  }

  provisioner "local-exec" {
    when    = destroy
    command = "rm -rf /tmp/public_ip.txt"
  }

  vpc_security_group_ids = [aws_security_group.ssh-access.id, aws_security_group.nginx-access.id]
}
