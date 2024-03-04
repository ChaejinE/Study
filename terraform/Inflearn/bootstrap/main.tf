terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "2.4.0" # > 1.0.0, < 2.4.0, != 1.2.0 or ~> 1.1.0
    }
  }
}

resource "local_file" "hello" {
  filename        = var.filename
  content         = random_string.random_code.id
  file_permission = "0777"

  depends_on = [random_string.random_code]

  lifecycle {
    create_before_destroy = true
  }

}

resource "random_string" "random_code" {
  length  = 5
  special = false
  upper   = false
}

output "random_code_output" {
  value       = random_string.random_code.id
  description = "id description test"
}

data "local_file" "world" {
  filename = "/tmp/word.txt"
}

resource "local_file" "test_count" {
  filename = var.filename_list[count.index]
  content = "test!!"
  count = length(var.filename_list)
}

resource "local_file" "test_for_each" {
  filename = each.value
  content = "test"
  for_each = var.file_set
}
