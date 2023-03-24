import motor.motor_asyncio
from model import Todo, User
from bson.objectid import ObjectId
from motorkey import motor_key 

client = motor.motor_asyncio.AsyncIOMotorClient(motor_key)
database = client.TodoList
collection = database.UserList
user_collection = database.user


async def fetch_all_todos(user : User):
    name = "Userlist" + user.username
    collection= database[name]

    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append({"_id": str(document["_id"]), 'desc':document['desc']})
    return todos

async def create_todo(todo : Todo, user : User):
    name = "Userlist" + user.username
    collection= database[name]

    validation = list(todo.values())[0]
    
    if validation == "":
        pass
    else:
        await collection.insert_one(todo)
        return todo
    
async def remove_todo(id, user : User):
    name = "Userlist" + user.username
    collection= database[name]

    await collection.delete_one({"_id": ObjectId(id)})
    return True

async def create_user(user):
    await user_collection.insert_one(dict(user))
    return user

async def user_exists(user):
    db_user = await user_collection.find_one({"username": user.username})
    try:
        if db_user["username"] == user.username:
            return False
    except:
        return True


async def db_fetch(user : User):
        db_match = await user_collection.find_one({"username": user.username})
        if db_match == None:
            return False
        return db_match
        # db_match["password"]

async def db_fetch2(username : str):
    db_match = await user_collection.find_one({"username": username})
    if db_match == None:
        return False
    return User(**db_match)
    # user.password


