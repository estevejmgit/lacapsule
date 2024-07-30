terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }
  
  # backend "local" {
  #   path = "my_state/terraform.tfstate"
  # }

  # backend "s3" {
  #   bucket  = "tfstate-jme-lacapsule"
  #   key     = "terraform/state"
  #   region = "eu-west-3"
  # }

  backend "http" {
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  region = "eu-west-3"
}

resource "aws_instance" "app_server" {
  ami           = "ami-0314c062c813a4aa0"
  instance_type = "t2.micro"
  key_name	= aws_key_pair.terraform-key.key_name
  
  vpc_security_group_ids = [data.aws_security_group.terraform-sg.id]

  tags = {
    Name = "terraform-test"
  }
}

#variable "security_group_id" {}

data "aws_security_group" "terraform-sg" {
  id = "sg-00a7fe3fdb054f43b"
}

resource "aws_key_pair" "terraform-key" {
  key_name   = "id_rsa"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABgQDWq7NeiuSegtIelrAnNJojAmYqAkLZ/hrvWR5LNmvJyqSvuU4D8BIcEr1O96WAFMXv8UMOe0baN9s3aryxcRutjIcGeTfoouSVWLe57PRkeI4b7vO0xnaAeujF3ZVvd68m4dFSlgdcdWpMDLlt4hVgp1WjyopowlqfHZZJ6sVspdEORuNi42SSTs2jLwuYYmuuloof/U2zH7rAbVVNb9kg/FWv2Fplp75S/3Ccr8uKRyt9FFDKvMUhuVZDH49ERJje6pFxjfGzeh7ZPQPlYbU+M4Z+VGZrYfLI9xUpk75nAv+yU8tMPpBRRrtZ1q7mVhMRRbb6TMiaK72H/IQQjn7Y8D9ZGUItkceyXlKOiObbvIgfHqwK1s5mE3dop78FxdV0LgMZWTENnZiwd9euTAb7JGNrAHj3d9zYQGi2Q9qnNwyW3SIhe15Gn0D1Ll512mAfE5JotWfRIvhwnhqNTqoUG7hrwmAF30pg40btToDAQexoESjULpoWGzHDKPg7tgU= jme@jme-VirtualBox"
}
