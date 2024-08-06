from typing import Literal
import json
import requests

type SOURCE_ID = Literal['nac_clients','reg_clients','server_hour','affected_agg','affected_data']
type METHOD = Literal['POST','GET']
class DataSource:
    """class with request data intrinsic"""
    source:dict[SOURCE_ID,str] = {
        #context data
        'nac_clients':'https://apps.sec.cl/INTONLINEv1/ClientesAfectados/GetClientesNacional',
        'reg_clients': 'https://apps.sec.cl/INTONLINEv1/ClientesAfectados/Get',
        'server_hour':'https://apps.sec.cl/INTONLINEv1/ClientesAfectados/GetHoraServer',
        #affected data
        'affected_total':'https://apps.sec.cl/INTONLINEv1/ClientesAfectados/Get',
        'affected_detail':'https://apps.sec.cl/INTONLINEv1/ClientesAfectados/GetPorFecha',        
    }
    def getData(self,source:SOURCE_ID,content_type:str='application/json,charset=utf-8',fetch_method:METHOD='POST'  )->json:
        
        req = requests.post(self.source[source])
        
        return {}
    
