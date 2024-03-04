# Basic structure
```
block_type "label" {
    key = value
    nested_block {
        key = value
    }
}
```

# Main commands
```bash
terraform init
```
- terraform provider, module download, version infomation(lock file)
- creation workspace
- creation tfstate
- default로 local에 tfstate를 저장

```bash
terraform plan
```
- add, change, destroy information

```bash
terraform apply
```
- apply, update

```bash
terraform destroy
```

```bash
terraform workspace list
terraform workspace new <name>
terraform workspace select <name>
terraform workspace delete <name>
```

# Links
- [Course](https://github.com/dimz119/learn-terraform)
- [Install](https://developer.hashicorp.com/terraform/tutorials/aws-get-started/install-cli)
- [Provider](https://registry.terraform.io/providers/hashicorp/local/latest/docs/resources/file)

# Manifests
- state file : apply에 대한 information. 보통 Storage 서비스 안에 넣어서 관리

# Provider

# Variables
- String, Number, Bool(true/false), List, Map({key = value}), etc...

```
variable <name> {
    type = ...
    default = ...
}
```
- Object : Complex data structure like JSON
- tuple, set, any
- When use like terraform.tfvars, terraform.tf vars.json, *.auto.tfvars, *.auto.tfvars.json, it is loaded

```bash 
terraform apply -var="key=val"
```
- As Top priority it is applied

```bash
terraform validate
```

```bash
terraform fmt
```
- pretty code

```bash
terraform show
```

```bash
terraform providers
```
- all providers versions, informations

```bash
brew install graphviz
terraform graph 
terraform graph | dot -Tsvg > sample.svg
```

# Attrivutes
## Implicit dependency
## Explicit dependency
```tf
resource "local_file" "hello" {
  filename = var.filename
  content = "${random_string.random_code.id}"
  file_permission = "0777"

  depends_on = [ random_string.random_code ]
}
 
resource "random_string" "random_code" {
  length = 5
  special = false
  upper = false
}
```

# Terraform Output
```bash
terraform ouptut -json > output.json
```

# tfstate
- JSON formatted state file
- State Tracking, Concurrency Management, Resource dependency, State preservation

# Features
- Mutable resources
  - eq) ec2 security group, tag
- Immutable resources
  - must destroy and recreate
  - eq) S3 Bucket Name, Encryption settings

## Lifecycle Rule
```tf
resource "local_file" "hello" {
  filename        = var.filename
  content         = random_string.random_code.id
  file_permission = "0777"

  depends_on = [random_string.random_code]

  lifecycle {
    create_before_destroy = true
  }
  
}
```
- create_before_destroy, prevent_destroy, ignore_changes

# META AGRUMENT
```tf
resource "local_file" "test_count" {
  filename = var.filename_list[count.index]
  content = "test!!"
  count = length(var.filename_list)
}

resource "local_file" "test_for_each" {
  filename = each.value
  content = "test"
  for_each = var.file_set
}
```
- count, for_each, depends_on, etc...


https://216917526503.signin.aws.amazon.com/console
terraform_user
znE'G4'Z

AKIATFAKKY7T2X2YNYGK
U6+SePx1RF88nfNtmiKMmOcV8c6S3em+D2bDsl/a