terraform {
  backend "s3" {
    bucket         = "cotton-terraform-dev-state"
    key            = "terraform.tfstate"
    region         = "eu-west-1"
    encrypt        = true
    dynamodb_table = "terraform_locks"
  }
}