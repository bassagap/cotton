# main.tf

provider "aws" {
  region = "eu-west-1"
}

resource "aws_instance" "flask_api_instance" {
  ami           = "ami-00c32bf891416bbd8"
  instance_type = "t2.micro"

  tags = {
    Name        = "flask-api-instance"
    Environment = "production"
    Project     = "cotton-dev-test-results-hub"
  }
  user_data = <<-EOF
              #!/bin/bash
              apt-get update
              apt-get install -y python3-pip
              pip3 install flask flask-restx
              EOF

  key_name = "cotton-dev-test-results-hub-api-kp"
}

resource "aws_security_group" "flask_api_security_group" {
  name        = "flask-api-security-group"
  description = "Security group for Flask API"

  ingress {
    from_port   = 5000
    to_port     = 5000
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

