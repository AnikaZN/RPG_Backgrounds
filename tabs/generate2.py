from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from joblib import load

from app import app
from .backstory import Character
from .traits import Traits
from .ideals import Ideals
from .bonds import Bonds
from .flaws import Flaws
from .why import Motivations
from .unique import Scams, Specialties, Routines, Events, Guilds, Reasons, Focuses, Ranks


style = {'padding': '1.5em'}

layout = html.Div([
    dcc.Markdown("""
        ### Your Character
        Use the controls below to generate your character's backstory based on their age.
    """),

    html.Div([
        dcc.Markdown('###### Age'),
        dcc.Slider(
            id='age',
            min=0,
            max=80,
            step=1,
            value="None",
            marks={n: str(n) for n in range(0, 85, 5)}
        )
    ], style=style),

    html.Div(id='events', style={'fontWeight':'bold'})

])


@app.callback(
    [Output('events', 'children')],
    [Input('age', 'value')])

def backstory(age):

    character = Character(age)

    events = "Life Events: ", character.life_events()

    all = events

    return all
