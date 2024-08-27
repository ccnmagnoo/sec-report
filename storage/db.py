from pandas import DataFrame
from models.Source import SOURCE_ID, DataSource as Api
from models.Payload import RegPayload, AffectedPayload #pylint: disable
from utils.transforms import deltatime_fmt, str2date

#cspell:disable

#data handler
api = Api()

# data getter
api.request(source='affected_detail',payload=AffectedPayload())
affected:DataFrame = api.dataframe(FECHA_INT_STR=str2date).copy()

## transform
### rename
affected = affected.rename(columns={
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
affected['periodo sin servicio']=affected['fecha incidente'].apply(deltatime_fmt)

###remove
affected = affected.drop(columns=['HORA','DIA','MES','ANHO'])


#store
storage:dict[SOURCE_ID,DataFrame] = {
    'affected_detail':affected
}