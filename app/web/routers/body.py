from fastapi import APIRouter, Body

body_router = APIRouter(prefix="/body", tags=["Http Requests"])

@body_router.post("/")
def post(name: str = Body(embed=True)):
    return {"name": name}

@body_router.post("/product")
def create_product(
    title: str = Body(title="Title", embed=True),
    price: int = Body(title="Price", embed=True, gt=0, le=100),
    is_active: bool = Body(title="Active status", embed=True)
):
    return {
        "title": title,
        "price": price,
        "is_active": is_active
    }