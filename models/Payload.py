from datetime import datetime, timedelta
import json
from typing import Literal

#cspell: disable
type REGION = Literal['Metropolitana','Tarapaca','Los Rios','Valparaiso','Biobio',\
    "O'Higgins",'Ñuble','La Araucania','Los Lagos','Aysén']
class Payload:
    """obtain json from"""
    def __init__(self, **kwargs:str) -> None:
        self.data = kwargs

    def __str__(self) -> str:
        """json object"""
        return json.dumps(self.data)

class DisconnectedPayload(Payload):
    """Payload for affected_detail"""
    def __init__(self, date:datetime=datetime.now(),delay_hours:int=0,delay_days:int=0) -> None:

        if delay_hours>0 or delay_days>0:
            #delay
            date = date - timedelta(hours=delay_hours,days=delay_days)
            self.report_date = date
        super().__init__(mes=date.month,dia=date.day,hora=date.hour,anho=date.year)

class RegPayload(Payload):
    """Payload for REG_CLIENTS or number regional clients data request"""
    def __init__(self, region:REGION) -> None:
        super().__init__(region=str(region))

if __name__=='__main__':
    payload = DisconnectedPayload()
    data = payload.data
    print('test',data)