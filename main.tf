
provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "upload_bucket" {
  bucket = "your-s3-bucket-name"
  acl    = "public-read"

  website {
    index_document = "index.html"
  }
}

resource "aws_iam_role" "lambda_exec" {
  name = "lambda_exec_role"
  assume_role_policy = file("assume-role-policy.json")
}

resource "aws_lambda_function" "log_uploads" {
  function_name = "log_uploads"
  handler       = "lambda_function.lambda_handler"
  runtime       = "python3.9"
  role          = aws_iam_role.lambda_exec.arn
  filename      = "lambda_function_payload.zip"
}
