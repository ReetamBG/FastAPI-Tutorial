# INTRO

from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def home():
    return 'Hello'


@app.post('/')
async def home_from_post():
    return 'Hello from post request'


# Start the app by using
# uvicorn file_name:app_name --reload --port=port_number

# --reload flag means server will autoreload once changes are saved (optional)
# --port number sets the port on which server is hosted (optional)

# here it will be
# uvicorn lec1:app --reload


# try using
# localhost:5000/docs route
# it will allow for debugging
