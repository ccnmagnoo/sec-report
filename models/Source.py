from typing import Literal
import json
from pandas import DataFrame
import requests
from models.Payload import Payload

type SOURCE_ID = Literal['nac_clients','reg_clients','server_hour','affected_agg','affected_data']
type METHOD = Literal['POST','GET']
class DataSource:
    """class with request data intrinsic"""
    _result = None
    source:dict[SOURCE_ID,str] = {
        #context data
        'nac_clients':'https://apps.sec.cl/INTONLINEv1/ClientesAfectados/GetClientesNacional',
        'reg_clients': 'https://apps.sec.cl/INTONLINEv1/ClientesAfectados/GetClientesRegional',
        'server_hour':'https://apps.sec.cl/INTONLINEv1/ClientesAfectados/GetHoraServer',
        #affected data
        'affected_total':'https://apps.sec.cl/INTONLINEv1/ClientesAfectados/Get',
        'affected_detail':'https://apps.sec.cl/INTONLINEv1/ClientesAfectados/GetPorFecha',
    }

    def request(self, source:SOURCE_ID,
                payload:Payload|None=None,
                content_type:str='application/json;charset=utf-8',
                fetch_method:METHOD='POST'  )->json:
        """web scrap request to www.sec.cl"""
        req = None

        match fetch_method:
            case 'POST':
                req = requests.post(
                    self.source[source],
                    data=payload.data,
                    # headers={'Content-Type':content_type},
                    timeout=500
                    )
            case 'GET':
                req = requests.get(
                    self.source[source],
                    data=payload.data,
                    # headers={'Content-Type':content_type},
                    timeout=500
                    )

        if req.status_code == 200:
            self._result = req.json()
            return {"status":200,"result":req.json()}
        else:
            return {"status":req.status_code}
        
    def dataframe(self)->DataFrame:
        pass

data_source:DataSource = DataSource()
