from fastapi import APIRouter

url_path_router = APIRouter(prefix="/url_path", tags=["Http Requests"])

@url_path_router.get("/{name}")
def url_path(name):
    return {"name": name}


