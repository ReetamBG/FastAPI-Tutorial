# PATH PARAMETERS

from fastapi import FastAPI

app = FastAPI()


@app.get('/users')
async def get_users():
    return {'message': 'These are the users'}


# # to get dynamic rendering
# @app.get('/users/{user_id}')
# async def get_user_by_id(user_id: int):    # add type hint or otherwise anything can be entered - now only /users/some_integer will work
#     return {'message': f'This is user {user_id}'}


# this won't work as the route above will take over
# /users/me - here 'me' will be taken as the parameter
# so it's always better to place it before the dynamic one ... always place static routes before the dynamic ones
@app.get('/users/me')
async def get_user_by_id():
    return {'message': f'This is the current user'}


# add dynamic route here after static one if similar routes
@app.get('/users/{user_id}')
async def get_user_by_id(user_id: int):
    return {'message': f'This is user {user_id}'}
