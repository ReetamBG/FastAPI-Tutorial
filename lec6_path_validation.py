# STRING AND NUMERIC VALIDATION IN PATH PARAMETERS
from importlib.resources import as_file

from fastapi import FastAPI, Query, Path
from typing import Annotated

app = FastAPI()


# Same as in Query parameters butt instead of Query() we use Path() on path parameters

# for string path parameter
@app.get("/users_string/{user_name}")
async def get_users(
		*,
		q: Annotated[str | None, Query()] = None,      # query parameter
		user_name: Annotated[int, Path(                # path parameter
			default=...,
			max_length=10,
			min_length=3,
			# regex = "some regex",
			alias="user_name",
			title="User Name",
			description="Path parameter for user name")]):

	return {"Query": q, "Path param": user_name}


# for numeric path parameter
@app.get("/users_numeric/{user_id}")
async def get_users(
		*,
		q: Annotated[int | None, Query(ge=0, le=10)] = None,    # query parameter
		user_id: Annotated[int, Path(
			max_digits=5,
			decimal_places=3,
			ge=20,
			le=30,
			# gt=20,
			# lt=30,
			alias="user_name",
			title="User ID",
			description="Path parameter for user id")]):

	return {"Query": q, "Path param": user_id}
