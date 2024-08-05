from typing import Literal

type SOURCE_ID = Literal['nac_clients','reg_clients','server_hour','affected_agg','affected_data']

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
