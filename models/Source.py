from typing import Literal
import json
import pandas as pd
from pandas import DataFrame
import requests
from models.Payload import Payload

type SOURCE_ID = Literal['nac_clients','reg_clients','server_hour','affected_agg','affected_detail']
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
        'affected_agg':'https://apps.sec.cl/INTONLINEv1/ClientesAfectados/Get',
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
                    json=payload.data,
                    #headers={'Content-Type':content_type},
                    timeout=60
                    )
            case 'GET':
                req = requests.get(
                    self.source[source],
                    json=payload.data,
                    #headers={'Content-Type':content_type},
                    timeout=60
                    )
            case _:
                return {"status":505,"result":"bad method"}
                

        if req.status_code == 200:
            self._result = req.json()
            return req.json()
        else:
            raise ValueError('bad request, error:',req.status_code)
        
    def dataframe(self)->DataFrame:
        """data stored in dataframe format"""
        if self._result is not None:
            return pd.DataFrame(self._result)
        else:
            raise ValueError('empty data, use request() method first')

data_source:DataSource = DataSource()
