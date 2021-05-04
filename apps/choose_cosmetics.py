#one of the pages of the app, where the person chooses its skintype and the product is recommended

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd
import pathlib
from app import app

# get relative data folder, we are doiing this, as the datasets are in the datasets folder, not the current directory
#PATH = pathlib.Path(__file__).parent
#DATA_PATH = PATH.joinpath("../datasets").resolve()

#dfv = pd.read_csv(DATA_PATH.joinpath("vgsales.csv"))
#sales_list = ["North American Sales", "EU Sales", "Japan Sales", "Other Sales",	"World Sales"]



layout = html.Div([
    html.H1("Choose cosmetics"),
    dcc.Dropdown( #dropdown for choosing skin type
            options=[
                {'label': 'Oily', 'value': 'ol'},
                {'label': 'Dry', 'value': 'dr'},
                {'label': 'Combo', 'value': 'cmb'},
                {'label': 'Not sure', 'value': 'ns'}
            ],
            value='MTL',
            multi = True
        )

])

