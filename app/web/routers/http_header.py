from fastapi import APIRouter, Header

http_header_router = APIRouter(prefix="/http_header", tags=["Http Requests"])

@http_header_router.get("/agent")
def header(user_agent: str = Header()):
    return {
        "user_agent": user_agent
    }