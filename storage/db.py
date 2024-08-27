from pandas import DataFrame
from models.Source import SOURCE_ID, DataSource as Api
from models.Payload import RegPayload, AffectedPayload
from utils.transforms import str2date

#data handler
api = Api()

#data getter
api.request(source='affected_detail',payload=AffectedPayload())

##transform
affected_detail:DataFrame = api.dataframe(FECHA_INT_STR=str2date)#dataFrame
affected_detail.rename(mapper={"NOMBRE_REGION":"Región"})

#store
storage:dict[SOURCE_ID,DataFrame] = {
    'affected_detail':affected_detail
}