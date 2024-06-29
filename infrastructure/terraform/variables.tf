variable region {
    type = string
    description = "Region where resource is created"
    default = "australia-southeast1"
}

variable project_id {
    type = string
    description = "GCP Project ID"
}

variable tf_service_account {
    type = string
    description = "Terraform service account"
}

