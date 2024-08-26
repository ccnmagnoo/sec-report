from typing import Literal
import json
import pandas as pd
from pandas import DataFrame
import requests
from models.Payload import Payload, AffectedPayload

type SOURCE_ID = Literal['nac_clients','reg_clients','server_hour','affected_agg','affected_detail']
type METHOD = Literal['POST','GET']
class DataSource:
    """class with request data intrinsic"""

    _result = None
    _payload:Payload|None = None

    _source:dict[SOURCE_ID,str] = {
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
                # content_type:str='application/json;charset=utf-8',
                fetch_method:METHOD='POST'  )->json:

        """web scrap request to www.sec.cl"""
        req = None
        self._payload=payload

        match fetch_method:
            case 'POST':
                req = requests.post(
                    self._source[source],
                    json=payload.data,
                    #headers={'Content-Type':content_type},
                    timeout=60
                    )
            case 'GET':
                req = requests.get(
                    self._source[source],
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

    @property
    def report_date(self):
        """return date of report of disconnected from electric service"""
        if isinstance(self._payload,AffectedPayload):
            return self._payload.report_date
    @property
    def result(self):
        return self._result
    
    def dataframe(self,**data_transforms:dict[str:callable])->DataFrame:
        """data stored in dataframe format"""
        #null point raise exception
        if self._result is None:
            raise ValueError('empty data, use request() method first')

        #define df instance
        df = pd.DataFrame(self._result)

        #no transforms return df
        if len(data_transforms)==0:
            return df

        #transforms apply
        for source,transform in data_transforms.items():
            df[source] = df[source].apply(transform)

        #return transformed
        return df

data_source:DataSource = DataSource()
