from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app, server
from tabs import personality, backstory

style = {'maxWidth': '960px', 'margin': 'auto'}

app.layout = html.Div([
    dcc.Markdown('# D&D Backstory Generator'),
    dcc.Tabs(id='tabs', value='tab-home', children=[
        dcc.Tab(label='Home', value='tab-home'),
        dcc.Tab(label='Personality', value='tab-personality'),
        dcc.Tab(label='Backstory', value='tab-backstory')
    ]),
    html.Div(id='tabs-content'),
], style=style)

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-home': return home.layout
    if tab == 'tab-personality': return personality.layout
    if tab == 'tab-backstory': return backstory.layout

if __name__ == '__main__':
    app.run_server(debug=True)
