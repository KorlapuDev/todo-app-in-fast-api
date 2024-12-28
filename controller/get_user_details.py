from config.models import users_collection


async def get_todo_name():
    user_email = "abhi@gmail.com"
    try:
        # storing into variable
        existing_user = users_collection.find_one({"email": user_email})
        result = {"name": existing_user["name"],
                  "todo_list": existing_user["todo_list"]}
        return result
    except Exception as err:
        return err
