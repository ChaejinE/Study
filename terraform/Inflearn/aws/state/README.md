```bash
terraform state list
```

```bash
terraform state show <resource_name>
```

```bash
terraform import <resource_type>.<resource_name> <resource_id>
```
- tfstate에 cli로 resource 넣는 방법
- Refactoring 시 추천

```bash
terraform state mv <resouce_address> <new_resource_address>
```
- 서비스화가 진행되면서, resource 이름을 바꿔야하는 경우가 많아진다.
- 바꾼 후에는 configuration은 수정을 해줘야된다.
- Refactoring 시 추천

```bash
terraform state rm <resource_address>
```
- managed by terraform resoucre 삭제. 하지만 실제 리소스가 삭제되지는 않고 state에서만 삭제된다.

```bash
terraform state pull
```
