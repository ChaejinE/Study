```bash
docker run --name mysqlDB -d --rm -it -e MYSQL_ROOT_PASSWORD=root123 -v ./mysql:/var/lib/mysql -p 3306:3306 mysql:latest
```
