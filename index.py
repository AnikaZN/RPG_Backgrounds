from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app, server
from tabs import generate

style = {'maxWidth': '960px', 'margin': 'auto'}

app.layout = html.Div([
    dcc.Markdown('# D&D Backstory Generator'),
    dcc.Tabs(id='tabs', value='tab-generate', children=[
        dcc.Tab(label='Home', value='tab-generate')
    ]),
    html.Div(id='tabs-content'),
], style=style)

@app.callback(Output('tabs-content', 'children'),
              [Input('tabs', 'value')])
def render_content(tab):
    if tab == 'tab-generate': return generate.layout

if __name__ == '__main__':
    app.run_server(debug=True)
