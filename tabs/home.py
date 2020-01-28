from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app

layout = [dcc.Markdown("""
### Intro

Greetings!

This web app allows you to generate a backstory and personality for your Dungeons and Dragons or
other RPG character.

Based on "Xanathar's Guide to Everything" and "The Player's Handbook" published by Wizards of the
Coast, this app simulates the dozens of dice rolls involved in generating a random, but fully
fleshed-out character.

As always, work with your DM/GM to incorporate these elements more fully into your game,
and have fun!
"""),

html.Img(src='/assets/dice-unsplash.jpg', style={'width':'100%'})]
