from dash import Dash, html, dcc
import plotly.express as px
from models.Payload import REGION
from storage.db import storage as data

#set app
app = Dash(__name__)

#data
reg:REGION ='Valparaiso'
current_report = data['affected_detail'][0]

# graphs
reg_pie = px.sunburst(
    current_report[current_report['región']==reg],
    values='afectados',
    color='afectados',
    color_continuous_scale='rdbu',
    path=['distribuidora','comuna'],
    hover_name='comuna',
    height=500
    )

bar_graph = px.bar(data['affected_detail'][0],x='región',y='afectados',color='afectados',width=50)

#app
app.layout = html.Div(children=[
    html.H1(children='clientes afectados'),
    # dcc.Graph(id='energy_quality',figure=bar_graph),
    dcc.Graph(id='service_by_city',figure=reg_pie),
    html.Div(children=[
        f'{current_report['afectados'].sum():,.0f} sin servicio',
        f'{data['reg_clients']:,.0f} clientes regionales'
    ])

])

#run
if __name__ == '__main__':
    app.run(debug=True)
