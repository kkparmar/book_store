variable region {
    type = string
    description = "Region where resource is created"
    default = "ap-southeast1"
}

variable project_id {
    type = string
    description = "GCP Project ID"
}

variable tf_service_account {
    type = string
    description = "Terraform service account"
}

variable state_bucket {
    type = string
    description = "Bucket where terraform state file is stored"
}

variable state_prefix {
    type = string
    description = "Bucket prefix for statefile"
}