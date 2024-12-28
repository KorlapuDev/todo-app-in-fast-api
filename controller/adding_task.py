from datetime import datetime

from config.models import users_collection


async def add_task_to_user(email: str, task:str):
    # Find the user by email (assuming email is unique)
    try:
        user_email = "laxman@gmail.com"

        new_task = {"Learn MongoDB": {task_name:task,task_status:"pending", end_date:str(datetime.utcnow())}}
        # storing into variable
        existing_user = users_collection.find_one({"email": user_email})
        if existing_user is None:
            return False
        # updating the dictionary
        existing_user['todo_list'].update(new_task)
        # updating it to the db
        updated_result = (
            users_collection.update_one({"email": user_email}, {"$set": existing_user}))
        # print(updated_result)
        if updated_result.raw_result["ok"] == 1.0:
            return existing_user
        return False
    except Exception as err:
        return err
