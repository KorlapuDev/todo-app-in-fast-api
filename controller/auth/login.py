from config.models import users_collection
from libs.helpers import jwt_creation_fun, password_check


async def login_auth(email, password):
    try:

        current_user = users_collection.find_one({"email": email},
                                                 {"_id": 0, "password": 1})
        check_res = await password_check(password, current_user["password"])

        if check_res is not True:
            return {"authrized": False, "token": ""}

        if current_user is None or not current_user:
            return {"authrized": False, "token": ""}
        # await jwt_creation_fun()
        token = await jwt_creation_fun(email)
        return {"authrized": True, "token": token}
    except Exception as err:
        return err
