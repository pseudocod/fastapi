from fastapi import FastAPI
from app.core.lifespan import lifespan  
import uvicorn

app = FastAPI(lifespan=lifespan)


@app.get("/")
def root():
    return {"message": "API is running"}

if __name__ == "__main__":
    uvicorn.run(
        "app.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )