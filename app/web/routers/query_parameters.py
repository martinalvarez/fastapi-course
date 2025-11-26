from fastapi import APIRouter

query_parameters_router = APIRouter(prefix="/query_parameters", tags=["Http Requests"])

@query_parameters_router.get("/")
def query_parameters(page: int, size: int, sort: str, order: str):
    return {
        "page": page,
        "size": size,
        "sort": sort,
        "order": order
    }
