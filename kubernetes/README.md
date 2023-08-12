# Kubernetes

# Ingress
## Nginx Install
```shell
cd Ingress
```

```shell
kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.0.0/deploy/static/provider/baremetal/deploy.yaml
```
- install

```shell
kubect get ns | grep nginx
```
- installation check : ```ingress-nginx```

### Service (IP)Load Balancing
```shell
cd service-loadbalacing
```

```shell
kubectl create ns my-app
```
- create namespace

```shell
kubect create -f customer.yaml
kubect create -f order.yaml
kubect create -f shopping.yaml
```
- deploy pods + services (App 3EA)

```shell
kubectl get svc -n my-app
```
```shell
# Cehck Examples
curl 10.105.234.52:8080
curl 10.107.203.128:8080
curl 10.103.90.152:8080
```
- service deploy check
- This isn't a case using ingress

```shell
kubectl apply -f ingress.yaml
```
- deploy ingress

```shell
kubectl get ingress -n my-app
```
```
NAME                    CLASS   HOSTS   ADDRESS         PORTS   AGE
service-loadbalancing   nginx   *       192.168.50.11   80      4m34s
```
- address checking

```shell
kubectl get svc -n ingress-nginx
```
```
NAME                                 TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)                      AGE
ingress-nginx-controller             NodePort    10.98.116.172   <none>        80:31406/TCP,443:30924/TCP   24m
ingress-nginx-controller-admission   ClusterIP   10.111.185.21   <none>        443/TCP                      24m
```
- http 31406 port checking

```shell
curl 192.168.50.11:31406/
Shopping Page.

curl 192.168.50.11:31406/order
Order Service.

curl 192.168.50.11:31406/customer
Customer Center.
```
- service check
- This is a case using ingress

### Canary Update
```shell
cd canary-update
```

```shell
kubectl create ns my-app2
```
- create namespace

```shell
kubectl create -f app-v1.yaml
kubectl create -f app-v2.yaml
kubectl create -f ingress.yaml
```
- deploy pods + services + ingress

```shell
cat << EOF >> /etc/hosts
192.168.50.11 www.app.com
EOF
```
- This is a way for using hostname

```shell
curl www.app.com:31406/version
```
```
Version : v1
```
- check

```shell
kubectl create -f ingress-canary.yaml
```
```yaml
annotations:
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-weight: "10"
```
- deploy ingress-canary.yaml
- setting canary update, weight (10%)

```shell
while true; do curl www.app.com:31406/version; sleep 1; done
```
- check 10% weight

```
Version : v1
Version : v1
Version : v1
Version : v1
Version : v2
Version : v1
Version : v1
Version : v1
Version : v1
Version : v1
Version : v2
Version : v1
...
```

```yaml
annotations:
    nginx.ingress.kubernetes.io/canary: "true"
    nginx.ingress.kubernetes.io/canary-by-header: "Accept-Language"
    nginx.ingress.kubernetes.io/canary-by-header-value: "kr"
```
- header

```shell
kubectl delete -f ingress-canary.yaml
kubectl create -f ingress-header.yaml
```

```shell
curl -H "Accept-Language: kr" www.app.com:31406/version
```
```
Version : v2
```
- It is responsive for specific header

# SSL
```shell
cd ssl
```

```shell
kubectl create ns my-app3
kubectl create -f app.yaml
kubectl create -f ingress.yaml
```

```shell
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout tls.key -out tls.crt -subj "/CN=www.https.com/O=www.https.com"
```
- create cert file (tls.crt, tls.key)

```shell
kubectl create secret tls secret-https --key tls.key --cert tls.crt -n my-app3
```
- deploy seceret

```
vim /etc/hosts

192.168.50.11 www.https.com
```

```
https://www.https.com:31406/hostname
```