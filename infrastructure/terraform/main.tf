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

resource "google_project_service" "sevices" {
  for_each = toset(local.enabled_apis)
  project = var.project_id
  service = each.value

}