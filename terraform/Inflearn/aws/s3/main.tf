provider "aws" {
  region = "us-west-2"
}

resource "aws_s3_bucket" "learn-terraform-mybucket" {
  bucket = "learn-terraform-mybucket-cjlotto"

  tags = {
    Environment = "devel"
  }
}

resource "aws_s3_bucket_public_access_block" "public-access" {
  bucket = aws_s3_bucket.learn-terraform-mybucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}

resource "aws_s3_object" "learn-terraform-smaple-text" {
  bucket = aws_s3_bucket.learn-terraform-mybucket.id
  key    = "sample.txt"
  source = "lotto.txt"
}

resource "aws_s3_bucket_policy" "bucket-policy" {
  bucket = aws_s3_bucket.learn-terraform-mybucket.id

  depends_on = [aws_s3_bucket_public_access_block.public-access]

  policy = <<POLICY
{
  "Version":"2012-10-17",
  "Statement":[
    {
      "Sid":"PublicRead",
      "Effect":"Allow",
      "Principal": "*",
      "Action":["s3:GetObject"],
      "Resource":["arn:aws:s3:::${aws_s3_bucket.learn-terraform-mybucket.id}/*"]
    }
  ]
}
POLICY
}
