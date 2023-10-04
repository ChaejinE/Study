from fastapi import FastAPI
from app.common.config import conf
import uvicorn

def create_app():
    c = conf()
    app = FastAPI()
    
    return app
    
app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
