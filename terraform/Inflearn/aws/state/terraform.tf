terraform {
  backend "s3" {
    bucket = "learn-terraform-remote-state-cjlotto"
    key= "terraform.tfstate"
    region = "us-west-2"
  }
}
