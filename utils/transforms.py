"""function utils to transform dataFrame from SEC api source"""
from datetime import datetime


def str2date(date_str:str)->datetime:
    "str format %d/%m/%Y"
    d,m,y = [int(it) for it in date_str.split('/')]
    return datetime(day=d,year=y,month=m)