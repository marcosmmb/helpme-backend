from models import SessionLocal, User, Alarm
from math import sqrt
from datetime import datetime, timedelta

db = SessionLocal()

RADIUS = 5
AGO = 10

def create_new_alarm(x, y):
    try:
        a = Alarm(x=x, y=y)
        db.add(a)
        db.commit()
        return a
    except:
        db.rollback()
        raise


def now_minus(minutes=10):
    now = datetime.utcnow()
    ago = timedelta(minutes=minutes)
    return now - ago


def get_alarm_by_radius(x, y, radius=RADIUS, ago=AGO):
    alarms = db.query(Alarm).filter(Alarm.creation >= now_minus(ago)).all()
    inside_alarms = list()
    for a in alarms:
        if sqrt((x - a.x) ** 2 + (y - a.y) ** 2) <= radius:
            inside_alarms.append(a)
    return inside_alarms
