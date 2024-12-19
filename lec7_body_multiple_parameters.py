# BODY - MULTIPLE PARAMETERS (MULTIPLE REQUEST BODIES)

from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Annotated

app = FastAPI()


class User(BaseModel):
	name: str
	age: int
	gender: str | None = None


class Item(BaseModel):
	name: str
	price: float


# Single Request Object
@app.post("/single_object")
async def get_single(user: User):
	return user


# Multiple Request Objects
@app.post("/multiple_objects")
async def get_multiple(
		user: User,
		item: Item | None = None
):
	response = {"user": user}
	if item:
		response.update({"item": item})

	return response


# Body parameter without BaseModel Class
@app.post("/singular_value")
async def get_singular_value(
		user_id: Annotated[int, Body()],
		user_name: Annotated[str | None, Body()] = None
):
	response = {"user_id": user_id}
	if user_name:
		response.update({"user_name": user_name})

	return response


# Embedding a single body parameter
@app.post("/embed")
async def embed(item: Annotated[Item, Body(embed=True)]):
	return item
