locals {
    enabled_apis = [
        "firestore.googleapis.com",
        "firebaserules.googleapis.com",
        "storage-api.googleapis.com",
        "artifactregistry.googleapis.com",
        "containerregistry.googleapis.com"
    ]

    bookstore_iam_roles = [
        "roles/run.developer",
        "roles/datastore.user",
        "roles/run.invoker",
        "roles/logging.bucketWriter",
        "roles/iam.serviceAccountUser",

    ]
}
