from fastapi import APIRouter
from controller.adding_task import add_task_to_user
# from fastapi.responses import JSONResponse
from responses import responses
from controller.get_user_details import get_todo_name
from controller.updating_task_details import task_status_change
protected_router = APIRouter()


@protected_router.post("/api/add_task")
async def add_task():
    result = await add_task_to_user()
    if result is False or result is None:
        content_res = responses["400"]
        content_res["message"] = "data is not updated"
        return content_res
    content_res = responses["200"]
    content_res["message"] = "data updated successfully"
    content_res["data"] = {"todo_list": result["todo_list"]}
    return {"response": content_res}


@protected_router.get("/api/get_tasks")
async def get_task():
    result = await get_todo_name()
    if result is False or result is None:
        content_res = responses["400"]
        content_res["message"] = "data is not fetched"
        return content_res
    content_res = responses["200"]
    content_res["message"] = "data is fetched successfully"
    content_res["data"] = result
    return {"response": content_res}


@protected_router.put("/api/update_task")
async def update_task_details():
    change_result = await task_status_change()

    if change_result.raw_result["ok"] != 1.0:
        content_res = responses["422"]
        content_res["message"] = "data is not updated"
        return {"response": content_res}

    result = await get_todo_name()
    if result is False or result is None:
        content_res = responses["400"]
        content_res["message"] = "data is not fetched"
        return content_res

    content_res = responses["200"]
    content_res["message"] = "task updated successfully"
    content_res["data"] = result
    return content_res
