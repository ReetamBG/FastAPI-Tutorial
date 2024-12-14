# QUERY PARAMETERS

from fastapi import FastAPI

app = FastAPI()


@app.get('/users/{user_id}')
async def get_user(user_id: int, user_name: str | None = None):

    # Here user_id is a path parameter and is used in the path and used like /users/3 or /users/4
    # But user_name is not present in the route definition, it is a query parameter and is used like /user/3?user_name='Ree'
    # We will ultimately remove it in post requests where we don't send the parameter through the path url

    return f'Hello {user_id} with name {user_name}'


# Using multiple path and query parameters
@app.get('/users/{user_id}/dashboard/{page_no}')
async def get_user(user_id: int, page_no: int, user_name: str | None = None, is_logged: bool = False):
    return f"""
    Hello {user_id} with name {user_name}
    You are on dashboard page {page_no}
    """
