terraform {
  required_providers {
    local = {
      source  = "hashicorp/local" # Provider
      version = "2.4.0" # Provider version
    }
  }

  required_version = ">= 1.4"
}

resource "local_file" "demo" {
    content = "hi. how are you ?"
    filename = "helloworld.txt"
}