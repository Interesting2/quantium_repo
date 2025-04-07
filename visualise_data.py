# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

sales_df = pd.read_csv("output.csv", delimiter=',')


app = Dash()

colors = {
    'background': '#FFFFE0',  # light yellow
    'text': '#333333',
    'subtext': '#800080'
}


fig = px.line(
    sales_df,
    x="date",
    y="sales"
)

fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

fig.add_vline(
    x=pd.to_datetime("2021-01-15"),
    line_width=2,
    line_dash="dash",
    line_color="red"
)

app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1("Pink Morsel Sales [2018-2022]",
            style={
                'textAlign': 'center',
                'color': colors['text']
            }
    ),
    html.Div("Were sales higher before or after the Pink Morsel price increase on the 15th of January, 2021?",
        style={
            'textAlign': "center",
            'color': colors['subtext']
        }
    ),
    dcc.Graph(
        id='Pink-Morsel-Sales',
        figure=fig
    ),
    html.H2("It's clear that the Pink Morsel Sales increased after 15th of January, 2021!",
        style={
            'textAlign': "center",
            'color': colors['subtext'],
            'fontSize': '20'

        }
    )
])

if __name__ == '__main__':
    app.run(debug=True)
