# STRING AND NUMERIC VALIDATION IN QUERY PARAMETERS

from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()


@app.get("/users1")
async def get_users1(name: str | None = Query(None)):
	# this is same as name: str|None = None
	# default value is set as Query(default_value)
	return {"name": name}


# with another default value
@app.get("/users2")
async def get_users2(name: str | None = Query("your name")):
	# this is same as name: str|None = "your name"
	return {"name": name}


# for mandatory query parameters (i.e. values without the "| None" part)
@app.get("/users3")
async def get_users3(
		name: Annotated[str, Query()]):
	# this is same as "name: str" and has no default value
	return {"name": name}


# for parameters with multiple value
@app.get("/users_multiple")
async def get_users_multiple(
		name: Annotated[list[str], Query()] = ["A", "B"]
):
	# now we can pass like /users_multiple?name="Ree"&name="Bee" as we have list[str]
	# default value is ["A", "B"]
	return {"name": name}    # name will return a list now


# other validation parameters

# for string
@app.get("/users_string/{user_id}")
async def get_users(
		user_id: int,
		query_param: str = Query(
			default=...,            # default value (Required as it is ...)
			max_length=10,          # maximum length of query
			min_length=3,           # minimum length of query
			# regex = "some regex"    # so that only query parameter matched with the regex is accepted
			alias="user_name",      # now instead of using /users/3?query_param="Ree", we need to use /users/3?user_name="Ree"
			title="some title",
			description="some description")):

	return {"query_param": query_param}


# for numeric query parameter (i.e. user_id: int = Query(...)
@app.get("/users_numeric/{user_id}")
async def get_users(
		user_id: int,
		query_param: int = Query(
			default=...,            # default value (Required as it is ...)
			max_digits=5,           # max digits (for numeric only)
			decimal_places=3,       # allowed number of digits after decimal
			ge=20,                  # greater than or equal to 10 (for numeric only)
			le=30,                  # less than or equal to 30 (for numeric only)
			# gt=20,                  # greater than
			# lt=30,                  # less than
			# regex = "some regex"    # so that only query parameter matched with the regex is accepted
			alias="user_name",      # now instead of using /users/3?name="Ree", we need to use /users/3?user_name="Ree"
			title="some title",
			description="some description")):

	return {"query_param": query_param}
