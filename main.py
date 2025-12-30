from fastapi import FastAPI
from database import create_db_and_tables
from controller import router
from fastapi.staticfiles import StaticFiles
import uvicorn

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(router)

if __name__=="__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)