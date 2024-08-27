"""function utils to transform dataFrame from SEC api source"""
from datetime import datetime, timedelta


def str2date(date_str:str)->datetime:
    "str format %d/%m/%Y"
    d,m,y = [int(it) for it in date_str.split('/')]
    return datetime(day=d,year=y,month=m)

def deltatime_fmt(event_date:datetime)->str:
    """returns readable delta time"""
    delta:timedelta = datetime.now()-event_date+timedelta(days=0)
    return f'{delta.days} dias {delta.seconds/3600:.0f} horas'
    