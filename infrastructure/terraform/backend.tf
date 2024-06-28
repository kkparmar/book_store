terraform {
    required_version = "~>0.18.0"
    backend "gcs" {
        bucket  = "tf-state-prod"
        prefix  = "terraform/state"
    }
    required_providers {
        google = {
            source = "hashicorp/google"
            version = "~>3.64.0"
        }
    }
}