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

backgrounds = ['Acolyte', 'Charlatan', 'Criminal', 'Entertainer', 'Folk Hero',
'Guild Artisan', 'Hermit', 'Noble', 'Outlander', 'Sage', 'Sailor', 'Soldier',
'Urchin']


style = {'padding': '1.5em'}

layout = html.Div([
    dcc.Markdown("""
        ### Your Character
        Use the controls below to generate a personality based on your character's background. The rest of your character's backstory will also be generated.
    """),

    html.Div([
        dcc.Markdown('###### Background'),
        dcc.Dropdown(
            id='background',
            options=[{'label': background, 'value': background} for background in backgrounds],
            value="None"
        ),
    ], style=style),

    html.Div([
        dcc.Markdown('###### Age'),
        dcc.Slider(
            id='age',
            min=0,
            max=80,
            step=1,
            value=10,
            marks={n: str(n) for n in range(0, 90, 10)}
        )
    ], style=style),

    html.Div(id='birthplace', style={'fontWeight':'bold'}),

    html.Div(id='siblings', style={'fontWeight':'bold'}),

    html.Div(id='flh', style={'fontWeight':'bold'}),

    html.Div(id='personality', style={'fontWeight':'bold'}),

    html.Div(id='events', style={'fontWeight':'bold'})

])


@app.callback(
    [Output('birthplace', 'children'),
     Output('siblings', 'children'),
     Output('flh', 'children'),
     Output('personality', 'children'),
     Output('events', 'children')],
    [Input('background', 'value'),
     Input('age', 'value')])

def backstory(background, age):

    character = Character(background, age)

    birthplace = character.birthplace()
    siblings = character.siblings()
    flh = character.family_lifestyle_home()
    personality = character.personality()
    events = character.life_events()

    all = birthplace, siblings, flh, personality, events

    return all
