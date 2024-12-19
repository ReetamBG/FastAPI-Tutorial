# REQUEST BODY ( FOR POST REQUESTS)

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


# Attributes of the request
class User(BaseModel):
    name: str
    age: int
    gender: str | None = None  # set to optional (may not be present in the post request) so can be none


# the post request from frontend will contain these attributes
# name, age and gender
# when we send a post request to /users with suppose name='Ree', age=20
# then in the get_users() function we will get the object 'user' with these attributes
# thus we need to make a class to store these request attributes what the frontend will send
# note that for request body the class must inherit the BaseModel from pydantic

# Uff why is it so complex can I not directly receive from frontend and check what I am receiving why do I have to make a class for receiving stuff??

# listen for post request on /user
@app.post('/users/{user_id}')
async def get_users(userid: int, user: User):       # user is of BaseModel class so FastAPI knows it is a request object
    print(user.name, user.age)                      # instead of request.name, we now have to use the class object for receiving and using the request parameters
    return user



# BENEFITS OF THIS ?? - Type checking. FastAPI will type check the request parameters (eg name must be str, age must be int, gender can be optional and so on)
# So this will throw error if any wrong data comes in through a request
