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
        Use the controls below to generate a personality based on your character's background The rest of your character's backstory will also be generated.

    """),

    html.Div([
        dcc.Markdown('###### Background'),
        dcc.Dropdown(
            id='background',
            options=[{'label': background, 'value': background} for background in backgrounds],
            value=backgrounds[0]
        ),
    ], style=style),

    html.Div(id='content', style={'fontWeight':'bold'}),

])


@app.callback(
    Output('content', 'children'),
    [Input('background', 'value')])

def backstory(background):

    character = Character(background)

    return character.personality(), character.birthplace(), character.siblings(), character.family_lifestyle_home()
