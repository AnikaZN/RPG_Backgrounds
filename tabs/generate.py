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
        Use the controls below to generate a personality based on your character's background.
    """),

    html.Div([
        dcc.Markdown('###### Background'),
        dcc.Dropdown(
            id='background',
            options=[{'label': background, 'value': background} for background in backgrounds],
            value="None"
        ),
    ], style=style),

    html.Div(id='birthplace', style={'fontWeight':'bold'}),

    html.Div(id='siblings', style={'fontWeight':'bold'}),

    html.Div(id='flh', style={'fontWeight':'bold'}),

    html.Div(id='personality', style={'fontWeight':'bold'}),

])


@app.callback(
    [Output('birthplace', 'children'),
     Output('siblings', 'children'),
     Output('flh', 'children'),
     Output('personality', 'children')],
     [Input('background', 'value')])

def personality(background, age):

    character = Character(background, age)

    birthplace = "Birthplace: ", character.birthplace()
    siblings = "SiblIngs: ", character.siblings()
    flh = "Lifestyle: ", character.family_lifestyle_home()
    personality = "Personality: ", character.personality()

    all = birthplace, siblings, flh, personality

    return all
