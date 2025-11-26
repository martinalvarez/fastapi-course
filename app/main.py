from fastapi import FastAPI
from app.web.routers.url_path import url_path_router
from app.web.routers.query_parameters import query_parameters_router
from app.web.routers.body import body_router
from app.web.routers.http_header import http_header_router


app = FastAPI()

app.include_router(url_path_router)
app.include_router(query_parameters_router)
app.include_router(body_router)
app.include_router(http_header_router)

@app.get("/")
def root():
    return {"message": "FastAPI is running"}
