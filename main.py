from controllers import (
    update_user_position,
    create_new_alarm,
    get_alarm_by_radius,
)
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title="HelpMe! API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["*"],
)

class UpdatePosition(BaseModel):
    email: str
    new_x: float
    new_y: float


class NewAlarm(BaseModel):
    x: float
    y: float


class PositionAndRadius(BaseModel):
    x: float
    y: float
    radius: float = 5.0
    ago: int = 10


# @app.post("/update_user_position")
# async def update_user_position_(up: UpdatePosition):
#     update_user_position(up.email, up.new_x, up.new_y)
#     return {"message": "Position updated to {}, {}".format(up.new_x, up.new_y)}


@app.post("/create_alarm")
async def create_alarm_(alarm: NewAlarm):
    """
    Criar alarme na posição x y
    Esse endpoint deve ser usado pelo botão (hardware)
    """
    create_new_alarm(alarm.x, alarm.y)
    return {"message": "New alarm created at {}, {}".format(alarm.x, alarm.y)}


@app.post("/get_near_alarms")
async def get_near_alarms(inp: PositionAndRadius):
    """
    Pegar alarmes dentro de um raio a partir de x, y que aconteceu há minutos
    Esse endpoint deve ser usado pelo app
    """
    r = get_alarm_by_radius(inp.x, inp.y, radius=inp.radius, ago=inp.ago)
    return {"alarms": r}
