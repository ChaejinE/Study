# Install
```bash
pipenv install kubeflow-katib
```

# Activate virtualenv
```bash
pipenv shell
```

# Reference
- https://www.kubeflow.org/docs/components/katib/overview/

# Custom
```bash
REPOSITORY=""
REGION=""
ECR_IMG=""
ECR_TAG=""
IMG="${REPOSITORY}/${ECR_IMG}:${ECR_TAG}"
```

## Running test
```bash
python custom.py --x 1 --y 2
```

## Deploy Experiment for hyperparameter tuning
```bash
NAMESPACE=""
python c_custom.py
```

## Docker Build & Push
```bash
aws ecr get-login-password --region ${REGION} | docker login --username AWS --password-stdin ${REPOSITORY}
docker build -f Dockerfile.custom -t custom:test .
docker tag test:test ${IMG}
docker push ${IMG}
```
