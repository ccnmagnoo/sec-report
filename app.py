from pprint import pp
from dash import Dash, html, dcc
import plotly.express as px
from models.Source import DataSource as Api
from models.Payload import RegPayload, AffectedPayload
from utils.transforms import str2date


#set app
app = Dash(__name__)

#data
api = Api()
api.request(source='affected_detail',payload=AffectedPayload())
events = api.dataframe(FECHA_INT_STR=str2date)

fig = px.bar(events,x='NOMBRE_REGION',y='CLIENTES_AFECTADOS',color='NOMBRE_EMPRESA',barmode='group')

#app
app.layout = html.Div(children=[
    html.H1(children='Clientes sin Servicio'),
    dcc.Graph(id='energy_disconnes',figure=fig)
])

#run
if __name__ == '__main__':
    app.run(debug=True)