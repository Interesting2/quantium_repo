# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

sales_df = pd.read_csv("output.csv", delimiter=',')


app = Dash()

colors = {
    'background': '#FFF1FF',
    'text': '#333333',
    'subtext': '#800080',
    'accent': '#4CAF50'
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

    html.Div([
        html.Label("Select a region:", style={'color': colors['text'], 'font-weight': 'bold', 'margin-bottom': '10px'}),
         dcc.RadioItems(
            options = {
                'north': 'north',
                'east': 'east',
                'south': 'south',
                'west': 'west',
                'all': 'all'
            },
            value='all',
            id='radio-region',
            labelStyle={'display': 'inline-block', 'margin-right': '20px', 'color': colors['accent']}

        )
    ], style={'margin': '20px', 'textAlign': 'center', 'margin-bottom': '30px'}),
   

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

@callback(
    Output('Pink-Morsel-Sales', 'figure'),
    Input('radio-region', 'value'))
def update_figure(selected_region):
    
    filtered_df = sales_df
    if selected_region != 'all':
        filtered_df = sales_df[sales_df.region == selected_region]

    fig = px.line(
        filtered_df,
        x="date",
        y="sales"
    )
    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text'],
        transition_duration=500
    )

    fig.add_vline(
        x=pd.to_datetime("2021-01-15"),
        line_width=2,
        line_dash="dash",
        line_color="red"
    )

    return fig


if __name__ == '__main__':
    app.run(debug=True)
