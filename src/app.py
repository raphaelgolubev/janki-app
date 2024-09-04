from fastapi import FastAPI


fastapi_app = FastAPI()


@fastapi_app.get("/")
def root():
    return {"message": "Hello World"}
