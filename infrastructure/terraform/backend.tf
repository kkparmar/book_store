terraform {
    required_version = "~>1.8.0"
    backend "gcs" {
        bucket  = "tf-state-prod"
        prefix  = "terraform/state"
    }
    required_providers {
        google = {
            source = "hashicorp/google"
            version = "~>5.30.0"
        }
    }
}