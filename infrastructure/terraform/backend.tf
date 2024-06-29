terraform {
    required_version = "~>1.8.0"
    backend "gcs" {
        bucket  = var.state_bucket
        prefix  = var.state_prefix
    }
    required_providers {
        google = {
            source = "hashicorp/google"
            version = "~>5.30.0"
        }
    }
}