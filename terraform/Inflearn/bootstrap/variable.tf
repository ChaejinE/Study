variable "filename" {
  default     = "/tmp/hello.txt"
  type        = string
  description = "local file name"
}

variable "content" {
  default = "Hello World!!!!"
}

variable "filename_list" {
  default = ["/tmp/1.txt", "/tmp/2.txt", "/tmp/3.txt"]
}

variable "file_set" {
  type    = set(string)
  default = ["/tmp/4.txt", "/tmp/5.txt", "/tmp/6.txt"]
}