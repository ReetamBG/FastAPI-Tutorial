# BODY - FIELDS

# Same as Query(), Path(), and Body() for metadata and data validation but for Request objects

from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()


class User(BaseModel):
	name: Annotated[str, Field(
		title="Name",
		description="Name of User",
		min_length=1,
		max_length=30,
	)] = "Name"

	age: Annotated[int, Field(
		title="Age",
		description="Age of User",
		gt=0,
		lt=100,
		# max_digits=2,      for some reason max_digits is giving error on Field() and Body()
	)]


@app.post("/path1")
async def path1(user: User):
	return user


# For single value request we can use the Body() (same parametes as Query and Path)
@app.post("/path2")
async def path2(
		*,

		user_id: Annotated[int, Body(
			title="ID",
			description="User ID of User",
			gt=0,
			lt=10000,
		)] = 9999,

		user_name:  Annotated[str, Body(
			title="Name",
			description="Name of User",
			min_length=1,
			max_length=30
		)]
):
	return {"user": user_id, "name": user_name}
