terraform {
  required_version = ">=1.0"
  backend "local" {}
  required_providers {
    google = {
      source = "hashicorp/google"
      version = "4.31.0"
    }
  }
}

provider "google" {
  project = var.project
  region = var.region
  // credentials = file(var.credentials) # can use this instead of setting env variable export statement (export GCP_AQUASIGNUM_CREDENTIALS="")
}