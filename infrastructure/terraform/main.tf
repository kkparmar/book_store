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