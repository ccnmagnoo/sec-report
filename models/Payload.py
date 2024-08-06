from datetime import datetime
import json
from typing import Literal

#cspell: disable
type REGION = Literal['Metropolitana','Tarapaca','Los Rios','Valparaiso','Biobio',\
    "O'Higgins",'Ñuble','La Araucania','Los Lagos','Aysén']
class Payload:
    """obtain json from"""
    def __init__(self,*args:str, **kwargs:str) -> None:
        print('loading keys:',kwargs,'values:',args)
        self.data = kwargs

    def __str__(self) -> str:
        """json object"""
        return json.dumps(self.data)

class SecPayload(Payload):
    """Payload for affected_detail"""
    def __init__(self, date:datetime=datetime.now()) -> None:
        super().__init__(month=date.month,day=date.day,hour=date.hour,anho=date.year)
        
class RegPayload(Payload):
    """Payload for REG_CLIENTS post request"""
    def __init__(self, region:REGION) -> None:
        super().__init__(region=str(region))


if __name__=='__main__':
    payload = SecPayload()
    data = payload.data
    print('test',data)