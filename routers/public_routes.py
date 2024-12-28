from fastapi import APIRouter, Form

from controller.auth.login import login_auth
from controller.auth.register import register_to_db
from helpers.api_response import get_response
from responses import responses

public_router = APIRouter()


@public_router.post("/login")
async def login(email: str = Form(...), password: str = Form(...)):

    authrized_user = await login_auth(email, password)

    if authrized_user["authrized"] is not True:
        return get_response("401", "user unauthrized")

    data = {"token": authrized_user["token"]}
    return get_response("200", "login successfull", data)


@public_router.post("/register")
async def register(email: str = Form(...), password: str = Form(...),
                   name: str = Form(...), occupation: str = Form(...)):
    # print(name, email, occupation, password)
    user_registration = await register_to_db(email, password, name, occupation)

    if user_registration["authrized"] is False:
        return get_response("401", "user not registered")

    data = {
        "token": user_registration["token"]
    }
    return get_response("200", "registration successfull", data)
