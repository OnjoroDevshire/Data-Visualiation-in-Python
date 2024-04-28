

from dash import Dash
from dash import dcc
from dash import html
import pandas as pd
import dash_auth
from dash.dependencies import Input, Output


data = pd.read_csv("tomatoe2.csv")
data = data.query("(type=='Ordinary') and (region=='Baraton' or region=='Tupcho' or region=='Chemundu')")

data["Date"] = pd.to_datetime(data["Date"], format="%d/%m/%Y")
data.sort_values("Date", inplace=True)
regions = ["Baraton", "Tupcho", "Chemundu"]


VALID_USERNAME_PASSWORD_PAIRS = [
    ["group1", "group1"],
    ["group2", "group2"],
    ["group3", "group3"]
]


app = Dash(__name__)

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)


app.layout = html.Div(
    children=[
        html.H1(
            children=[
                "Tomato Sale Analyst",
                html.Img(src='images\tomatoes.png', style={'height':'50px', 'margin-left': '10px'})
            ],
            style={
                "textAlign": "center",
                "color": "white",
                "fontSize": "50px",
                "marginTop": "50px",
                "backgroundColor": "black",
                "display": "flex",
                "align-items": "center",
                "justify-content": "center",
                "padding": "20px"
            }
        ),

        html.P(
            children="Analyze the varying behavior of tomato prices"
            " and the total Volume of tomatoes  sold in Baraton"
            " in 2023",
            style={
                "textAlign": "center",
                "color": "#008080",
                "fontSize": "24px",
                "marginBottom": "50px",
            },
        ),

        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["AveragePrice"],
                        "type": "lines",
                    },
                ],
                "layout": {
                    "title": "Average price of Tomatoes",
                    "plot_bgcolor": "black",
                    "paper_bgcolor": "black",
                    "font": {"color": "#008080"},
                    "xaxis": {"gridcolor": "#e6e6e6"},
                    "yaxis": {"gridcolor": "#e6e6e6"},
                },
            },
            style={"height": "500px", "marginBottom": "50px"},
        ),
         dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Total Volume"],
                        "type": "lines",
                    },
                ],
                "layout": {
                    "title": "Total Volume of Tomatoes sold in Baraton",
                    "plot_bgcolor": "black",
                    "paper_bgcolor": "black",
                    "font": {"color": "#008080"},
                    "xaxis": {"gridcolor": "#e6e6e6"},
                    "yaxis": {"gridcolor": "#e6e6e6"},
                },
            },
            style={"height": "500px", "marginBottom": "50px"},
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["region"],
                        "y": data["Total Volume"],
                        "type": "bar",
                    },
                ],
                "layout": {
                    "title": "Total Volume of Tomatoes sold by Region",
                     "plot_bgcolor": "black",
                    "paper_bgcolor": "black",
                    "font": {"color": "#008080"},
                    "xaxis": {"gridcolor": "#e6e6e6"},
                    "yaxis": {"gridcolor": "#e6e6e6"},
                },
            },
            style={"height": "500px", "marginBottom": "50px"},
        ),
    ],
    style={"maxWidth": "1200px", "margin": "0 auto"},
)

if __name__ == "__main__":
    app.run_server(debug=True)
