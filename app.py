from dash import Dash, html, dcc
import plotly.express as px
from storage.db import storage as data

#set app
app = Dash(__name__)

#graphs
bar_graph = px.bar(data['affected_detail'],x='NOMBRE_REGION',y='CLIENTES_AFECTADOS',barmode='group')

#app
app.layout = html.Div(children=[
    html.H1(children='Clientes sin Servicio'),
    dcc.Graph(id='energy_disconnes',figure=bar_graph)
])

#run
if __name__ == '__main__':
    app.run(debug=True)