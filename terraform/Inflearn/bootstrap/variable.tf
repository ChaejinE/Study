variable "filename" {
  default     = "/tmp/hello.txt"
  type        = string
  description = "local file name"
}

variable "content" {
  default = "Hello World!!!!"
}
