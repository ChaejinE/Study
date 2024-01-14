# Reference
- https://fastapi.tiangolo.com/ko/

# on Local
## Setup
```bash
pipenv install --deploy
```

## Run
```bash
uvicorn main:app --reload
```
- main : main.py file name
- app : created object in main.py ```app = FastAPI()```
- --reload : When raised modification code, restart app. use only when developing

# API Docs
- Swagger UI
```
http://127.0.0.1:8000/docs
```

```
http://127.0.0.1:8000/redoc
```
