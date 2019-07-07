from controllers import create_new_alarm, get_alarm_by_radius
from models import Alarm


def test_create_new_alarm():
    new_alarm = create_new_alarm(0, 0)
    assert isinstance(new_alarm, Alarm)
    try:
        create_new_alarm("ola", "mundo")
        assert False
    except:
        pass


def test_get_alarm_by_radius():
    alarms = get_alarm_by_radius(0, 0, 0, 2)
    assert isinstance(alarms, list)
    assert len(alarms) >= 1
