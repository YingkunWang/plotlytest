# import pandas as pd
# import dash_core_components as dcc
# import plotly.express as px
# import dash_table
# import dash_html_components as html
#
# df2 = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')
#
# output = html.Div(id = 'output',
#                 children = [],
#                 )
#
# fig = px.scatter(df2, x="gdp per capita", y="life expectancy",
#                  size="population", color="continent", hover_name="country",
#                  log_x=True, size_max=60)
#
# def App2():
#     layout = html.Div([
#         output
#     ])
#     return layout
#
#
# def build_graph(city):
#     graph = dcc.Graph(
#                figure = fig,
#                  )
#     return graph

### Data
import pandas as pd
import pickle
### Graphing
import plotly.graph_objects as go
### Dash
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
## Navbar
from navbar import Navbar
df = pd.read_csv('https://gist.githubusercontent.com/joelsewhere/f75da35d9e0c7ed71e5a93c10c52358d/raw/d8534e2f25495cc1de3cd604f952e8cbc0cc3d96/population_il_cities.csv')
df.set_index(df.iloc[:,0], drop = True, inplace = True)
df = df.iloc[:,1:]

nav = Navbar()

header = html.H3(
    'Page1 Test!'
)

options = [{'label':x.replace(', Illinois', ''), 'value': x} for x in df.columns]

dropdown = html.Div(dcc.Dropdown(
    id = 'pop_dropdown',
    options = options,
    value = 'Abingdon city, Illinois'
))


output = html.Div(id = 'output',
                children = [],
                )

def App2():
    layout = html.Div([
        nav,
        header,
        dropdown,
        output
    ])
    return layout


def build_graph(city):
    data = [go.Scatter(x = df.index,
                            y = df[city],
                            marker = {'color': 'orange'})]
    graph = dcc.Graph(
               figure = {
                   'data': data,
    'layout': go.Layout(
                        title = '{} Population Change'.format(city),
                        yaxis = {'title': 'Population'},
                        hovermode = 'closest'
                                      )
                           }
                 )
    return graph
