# dash_app.py
from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import requests

dash_app = Dash(
    __name__,
    requests_pathname_prefix="/mapStats/"
)


dash_app.layout = html.Div([
    html.H1("Map Statistics Dashboard", className="mb-4"),
    
    # Filters
    html.Div([
        html.Div([
            html.Label("Enemy Quality Filter:", className="font-bold"),
            dcc.Dropdown(
                id='enemy-quality-filter',
                multi=True,
                options=[
                    {'label': 'Ty1+', 'value': 'Ty1+'},
                    {'label': 'Low', 'value': 'Low'}
                ],
                placeholder="Select Enemy Quality..."
            )
        ], className="w-1/2 pr-2"),

    dcc.Store(id='clan-data', data=[]),
    html.Div([
        html.Label("Clan Filter:", className="font-bold"),
        dcc.Dropdown(
            id='clan-filter',
            options=[],  # Start empty
            multi=False,
            placeholder="Select Clan..."
        )
    ]),
        
        html.Div([
            html.Label("Team Filter:", className="font-bold"),
            dcc.Dropdown(
                id='team-filter',
                options=[
                    {'label': 'Team A', 'value': 'A'},
                    {'label': 'Team B', 'value': 'B'}
                ],
                multi=True,
                placeholder="Select Team..."
            )
        ], className="w-1/2 pl-2")
    ], className="flex mb-4"),
    
    # Graph
    dcc.Graph(id='map-stats-graph'),
    
    # Data refresh interval
    dcc.Interval(
        id='interval-component',
        interval=60*1000,  # refresh every minute
        n_intervals=0
    )
])

@dash_app.callback(
    Output('clan-filter', 'options'),
    Input('clan-data', 'data'),  # This will trigger once when the page loads
)
def initialize_clans(data):
    response = requests.get('http://localhost:8000/clans/tracked')
    data = response.json()
    df = pd.DataFrame(data).set_index('TrackedClanID')
    clans = sorted(df['Tag'].unique())
    return [{'label': clan, 'value': clan} for clan in clans]

@dash_app.callback(
    Output('map-stats-graph', 'figure'),
    [Input('enemy-quality-filter', 'value'),
     Input('team-filter', 'value'),
     Input('interval-component', 'n_intervals'),
     Input('clan-filter', 'value')]
)
def update_graph(selected_qualities, selected_teams, n, selected_clan):
    # Fetch data
    if selected_clan:
        # Fix the URL formatting
        url = f'http://localhost:8000/cb/gamelist?ClanTag={selected_clan}&Season=28'
        response = requests.get(url)
    else:
        return {
            'data': [],
            'layout': {
                'title': 'Please select a clan',
                'xaxis': {'title': 'Map'},
                'yaxis': {'title': 'Number of Games'}
            }
        }
    
    try:
        data = response.json()
        if not data:  # Handle empty response
            return {
                'data': [],
                'layout': {
                    'title': 'No data available for selected clan',
                    'xaxis': {'title': 'Map'},
                    'yaxis': {'title': 'Number of Games'}
                }
            }
        
        # Create DataFrame and ensure it has an index
        df = pd.DataFrame(data)
        
        # Apply filters
        if selected_qualities:
            df = df[df['EnemyQuality'].isin(selected_qualities)]
        if selected_teams:
            df = df[df['TeamAB'].isin(selected_teams)]
        
        # Check if DataFrame is empty after filtering
        if df.empty:
            return {
                'data': [],
                'layout': {
                    'title': 'No data available after applying filters',
                    'xaxis': {'title': 'Map'},
                    'yaxis': {'title': 'Number of Games'}
                }
            }
        
        # Prepare data for stacked bar chart
        results_by_map = df.groupby('Map').agg({
            'Result': lambda x: (x == 1).sum(),  # Wins
            'Map': 'count'  # Total games
        }).rename(columns={'Result': 'Wins', 'Map': 'Total'})
        
        results_by_map['Losses'] = results_by_map['Total'] - results_by_map['Wins']
        
        return {
            'data': [
                {
                    'name': 'Wins',
                    'type': 'bar',
                    'x': results_by_map.index,
                    'y': results_by_map['Wins'],
                    'marker': {'color': 'green'}
                },
                {
                    'name': 'Losses',
                    'type': 'bar',
                    'x': results_by_map.index,
                    'y': results_by_map['Losses'],
                    'marker': {'color': 'red'}
                }
            ],
            'layout': {
                'title': f'Wins and Losses by Map for {selected_clan}',
                'barmode': 'stack',
                'xaxis': {'title': 'Map'},
                'yaxis': {'title': 'Number of Games'},
                'legend': {'orientation': 'h', 'y': 1.1}
            }
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'data': [],
            'layout': {
                'title': f'Error processing data: {str(e)}',
                'xaxis': {'title': 'Map'},
                'yaxis': {'title': 'Number of Games'}
            }
        }