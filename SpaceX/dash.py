# Import required libraries
import pandas as pd
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Read the SpaceX data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")

max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[
    html.H1(
        'SpaceX Launch Records Dashboard',
        style={'textAlign': 'center',
               'color': '#503D36',
               'font-size': 40}
    ),

    # TASK 1: Launch Site Drop-down
    dcc.Dropdown(
        id='site-dropdown',
        options=[{'label': 'All Sites', 'value': 'ALL'}] + [
            {'label': site, 'value': site}
            for site in spacex_df['Launch Site'].unique()
        ],
        value='ALL',
        placeholder='Select a Launch Site here',
        searchable=True
    ),
    html.Br(),

    # TASK 2: Pie chart
    dcc.Graph(id='success-pie-chart'),
    html.Br(),

    html.P("Payload range (Kg):"),

    # TASK 3: RangeSlider
    dcc.RangeSlider(
        id='payload-slider',
        min=0,
        max=10000,
        step=1000,
        value=[min_payload, max_payload],
        marks={
            0: '0',
            2500: '2500',
            5000: '5000',
            7500: '7500',
            10000: '10000'
        }
    ),
    html.Br(),

    # TASK 4: Scatter chart
    dcc.Graph(id='success-payload-scatter-chart')
])

# TASK 2: Callback for pie chart
@app.callback(
    Output(component_id='success-pie-chart', component_property='figure'),
    Input(component_id='site-dropdown', component_property='value')
)
def get_pie_chart(entered_site):
    # ALL sites selected
    if entered_site == 'ALL':
        # Toplam başarı sayısını site bazında göster
        df = spacex_df[spacex_df['class'] == 1]
        fig = px.pie(
            df,
            names='Launch Site',
            title='Total Successful Launches for All Sites'
        )
    else:
        # Seçili site için success vs failure (class = 1 vs 0)
        df = spacex_df[spacex_df['Launch Site'] == entered_site]
        fig = px.pie(
            df,
            names='class',
            title=f'Success vs Failure for {entered_site}'
        )
    return fig

# TASK 4: Callback for scatter chart
@app.callback(
    Output(component_id='success-payload-scatter-chart', component_property='figure'),
    [
        Input(component_id='site-dropdown', component_property='value'),
        Input(component_id='payload-slider', component_property='value')
    ]
)
def get_scatter_chart(entered_site, payload_range):
    low, high = payload_range

    # Önce payload aralığına göre filtrele
    mask = (spacex_df['Payload Mass (kg)'] >= low) & \
           (spacex_df['Payload Mass (kg)'] <= high)
    df = spacex_df[mask]

    # Sonra site filtresi
    if entered_site != 'ALL':
        df = df[df['Launch Site'] == entered_site]

    # Scatter: payload vs class, renk = Booster Version Category
    fig = px.scatter(
        df,
        x='Payload Mass (kg)',
        y='class',
        color='Booster Version Category',
        title='Payload vs Launch Outcome'
    )
    return fig


# Run the app
if __name__ == '__main__':
    app.run()
