from typing import Literal
from pandas import DataFrame
from models.Source import SOURCE_ID, DataSource as Api
from models.Payload import Payload, RegPayload, AffectedPayload #pylint: disable
from utils.transforms import deltatime_fmt, str2date

#cspell:disable
type Params = Literal[
    'día',
    'mes',
    'año',
    'región',
    'comuna',
    'afectados',
    'distribuidora',
    'fecha incidente',
    'actualización'
    ]

#data handler
api = Api()

# fetch data
## total clients
api.request(source='reg_clients',payload=RegPayload(region='Valparaiso'))
reg_clients = int(api.result[0]['CLIENTES']) #json
api.request(source='nac_clients',payload=Payload())
nac_clients = int(api.result[0]['CLIENTES']) #json


## affected data
delay_folder = [
    {'delay_hours':0},
    {'delay_hours':1},
    {'delay_hours':6},
    {'delay_hours':12},
    {'delay_hours':24}
    ]
drawer:list[DataFrame] = []
for delay in delay_folder:
    api.request(source='affected_detail',payload=AffectedPayload(**delay))
    result:DataFrame = api.dataframe(FECHA_INT_STR=str2date).copy()
    
    ## transform
    
    ### rename
    result = result.rename(columns={
        "DIA_INT":"día",
        "MES_INT":"mes",
        "ANHO_INT":"año",
        "NOMBRE_REGION":"región",
        "NOMBRE_COMUNA":"comuna",
        "NOMBRE_EMPRESA":"distribuidora",
        "ACTUALIZADO_HACE":"actualización",
        "FECHA_INT_STR":"fecha incidente",
        "CLIENTES_AFECTADOS":"afectados",
        })


    ###calculate columns
    result['periodo sin servicio']=result['fecha incidente']\
        .apply(lambda event:deltatime_fmt(event_date=event,report_date=api.report_date))

    ###remove
    result = result.drop(columns=['HORA','DIA','MES','ANHO'])
    
    ###compose object

    ###append
    drawer.append(result)


#store
storage:dict[SOURCE_ID,DataFrame|list[DataFrame]] = {
    'affected_detail':drawer,
    'reg_clients':reg_clients,
    'nac_clients':nac_clients,
}