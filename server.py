import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from helpers.api_response import get_response
from routers.protected_routes import protected_router
from routers.public_routes import public_router

app = FastAPI()

origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/check")
def hell_check() -> dict:
    return get_response('200', "ToDo app is workinng.")


app.include_router(public_router, prefix="/api")
app.include_router(protected_router, prefix="/auth")

if __name__ == "__main__":
    uvicorn.run("server:app", host="127.0.0.1", port=4000, reload=True)

