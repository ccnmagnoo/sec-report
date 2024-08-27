from dash import Dash, html, dcc
import plotly.express as px
from storage.db import storage as data

#set app
app = Dash(__name__)

#graphs
print(data)
bar_graph = px.bar(data['affected_detail'][0],x='región',y='afectados',color='afectados',width=50)

#app
app.layout = html.Div(children=[
    html.H1(children='clientes afectados'),
    dcc.Graph(id='energy_quality',figure=bar_graph)
])

#run
if __name__ == '__main__':
    app.run(debug=True)
