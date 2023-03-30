from datetime import datetime
import pytz


UTC = pytz.utc
IST = pytz.timezone('Europe/Kiev')



def get_current_datetime():
    return datetime.now(IST)
    