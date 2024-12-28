from pymongo import MongoClient

# creating a client
client = MongoClient('mongodb://localhost:27017/')


# Accessing the database
db = client['user']

# Accessing the collection
users_collection = db['users']

user_data = {
    "email": "nitin@gmail.com",
    "password": "nitin1372",
    "name": "Nitin",
    "occupation": "SDE-2",
    "todo_list": {
        "Learn Nextjs": [
            "pending",
            "dateCreated"
        ],
        "Learn ReactNative": [
            "done",
            "dateCreated"
        ]
    }
}


# def add_task_to_db():
#     # Find the user by email (assuming email is unique)
#     user_email = "abhi@gmail.com"
#     existing_user = users_collection.find_one({"email": user_email})

#     # Add a new task with the current timestamp to the todo_list
#     # new_task = ["pending", str(datetime.utcnow())]
#     new_task = [{"Learn MongoDB": ["pending", str(datetime.utcnow())]}]

#     if "todo_list" not in existing_user:
#         existing_user["todo_list"] = {}

#     existing_user["todo_list"].update(new_task)
#     print("this is ex", existing_user)
#     # existing_user["todo_list"]["Learn MongoDB"].append(new_task)
#     users_collection.update_one({"email": user_email}, {"$set": existing_user})
#     return "done"


if __name__ == "__main__":
    # Insert data into the collection
    # users_collection.insert_one(user_data)
    print("Done")
