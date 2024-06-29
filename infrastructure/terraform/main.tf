# main.tf 

resource "random_string" "random" {
  length           = 16
  special          = true
  override_special = "/@£$"
}

output "random_string" {
    value = random_string.random.id
}

### enable apis

resource "google_project_service" "services" {
  for_each = toset(local.enabled_apis)
  project = var.project_id
  service = each.value
  disable_on_destroy = false

}

resource "google_firestore_database" "database" {
  project                     = var.project_id
  name                        = "(default)"
  location_id                 = var.region
  type                        = "FIRESTORE_NATIVE"
  concurrency_mode            = "OPTIMISTIC"
  app_engine_integration_mode = "DISABLED"

  depends_on = [google_project_service.services["firestore.googleapis.com"]]
}

## service account for bookstore application

resource "google_service_account" "bookstore_app" {
  account_id   = "bookstore-app-cr"
  display_name = "Service account for bookstore app being run in Cloud Run"
}



resource "google_service_account_iam_member" "bookstore_app_sa_iam" {
  for_each = toset(local.bookstore_iam_roles)
  service_account_id = data.google_compute_default_service_account.default.name
  role               = each.value
  member             = "serviceAccount:${google_service_account.sa.email}"
}
