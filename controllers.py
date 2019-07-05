from models import SessionLocal, User, Alarm
from math import sqrt
from datetime import datetime, timedelta

db = SessionLocal()

RADIUS = 5
AGO = 10


def create_new_user(email):
    u = User(email=email)
    try:
        db.add(u)
        db.commit()
        return u
    except:
        db.rollback()
        raise

def get_user_by_email(email):
    u = db.query(User).filter(User.email == email).first()
    return u


def get_user_position(email):
    u = get_user_by_email(email)
    return u.x, u.y


def update_user_position(email, new_x, new_y):
    try:
        u = get_user_by_email(email)
        if not u:
            u = create_new_user(email)
        u.x = float(new_x)
        u.y = float(new_y)
        db.commit()
        return (u.x, u.y)
    except:
        db.rollback()
        raise


def get_users_by_radius(x, y, radius=RADIUS):
    users = db.query(User).all()
    inside_users = list()
    for u in users:
        if sqrt((x - u.x) ** 2 + (y - u.y) ** 2) <= radius:
            inside_users.append(u)
    return inside_users


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
