from controllers import *
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UpdatePostion(BaseModel):
    email: str
    new_x: float
    new_y: float

@app.post("/update_position")
async def root(up: UpdatePostion):
    update_user_position(up.email, up.new_x, up.new_y)
    return {"message": "Position updated to {}, {}"
            .format(up.new_x, up.new_y)}