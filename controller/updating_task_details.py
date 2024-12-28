from config.models import users_collection


async def task_status_change():
    user_email = "abhi@gmail.com"
    try:
        # storing into variable
        existing_user = users_collection.find_one({"email": user_email})
        task_to_update = "Learn Nextjs"
        new_status = "done"
        result = users_collection.update_one(
            existing_user,
            {"$set": {f"todo_list.{task_to_update}.0": new_status}}
            )
        # print(existing_user)
        return result
    except Exception as err:
        return err
