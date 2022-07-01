from dash import Dash, html
import dash_cytoscape as cyto

app = Dash(__name__)

nodes = [
    {
        'data': {'id': short, 'label': label},
        'position': {'x': 20 * lat, 'y': -20 * long}, 
        'classes': color
    }
    for short, label, color, long, lat in (
        ('cz', 'Chi Z', 'blue', 34.03, -118.25),
        ('cl', 'Chang L', 'red', 40.71, -74),
        ('jy', 'Jing Y', 'red', 43.65, -79.38),
        ('plw', 'Pengluo W', 'blue', 45.50, -73.57),
        # ('yyt', 'Yuyi T', 'red', 49.28, -123.12),
        # ('xl', 'Xiao L', 'blue', 41.88, -87.63),
        ('zpy', 'Zhipeng Y', 'blue', 42.36, -71.06),
        ('qjf', 'Qiaojun F', 'blue', 29.76, -95.37),
        ('jx', 'Jing X', 'red', 29.76, -95.37),
        ('ylh', 'Yuli H', 'red', 29.76, -95.37),
        ('ayc', 'Anne', 'red', 29.76, -95.37),
        ('ysc', 'Yusi C', 'red', 29.76, -95.37),
        ('bz', 'Bill Zhan', 'blue', 29.76, -95.37),
        ('mlz', 'Menglin Zhou', 'red', 29.76, -95.37)
    )
]

edges = [
    {'data': {'source': source, 'target': target}, 'classes': linetype}
    for source, target, linetype in (
        ('cz', 'cl', 'solid'),
        ('cz', 'jy', 'solid'),
        ('cz', 'plw', 'solid'),
        ('cz', 'qjf', 'dashed'),
        ('cz', 'ylh', 'dashed'),
        ('cz', 'zpy', 'dashed'),
        ('cl', 'jy', 'solid'),
        ('cl', 'plw', 'solid'),
        ('cl', 'ayc', 'solid'),
        ('cl', 'jx', 'dashed'),
        ('jy', 'ayc', 'solid'),
        ('jy', 'plw', 'solid'),
        ('jy', 'jx', 'solid'),
        ('plw', 'qjf', 'solid'),
        ('plw', 'ylh', 'solid'),
        # ('plw', 'yyt', 'solid'),
        # ('plw', 'xl', 'solid'),
        ('plw', 'zpy', 'solid'),
        ('plw', 'ysc', 'solid'),
        ('plw', 'ayc', 'dashed'),
        ('plw', 'bz', 'solid'),
        ('plw', 'mlz', 'solid'),
        ('qjf', 'ylh', 'gold'),
        ('qjf', 'bz', 'solid'),
        ('ylh', 'bz', 'solid'),
        ('ylh', 'mlz', 'solid'),
        ('bz', 'mlz', 'gold'),
        # ('yyt', 'xl', 'gold'),
        # ('yyt', 'zpy', 'solid'),
        # ('xl', 'zpy', 'solid')
        
    )
]

elements = nodes + edges


app.layout = html.Div([
    cyto.Cytoscape(
        id='cytoscape-elements-basic',
        elements=elements,
        layout={'name': 'cose'},
        style={'width': '100%', 'height': '800px'}, 
        stylesheet=[
            # Group selectors
            {
                "selector": "node",
                "style": {
                    "content": "data(label)",
                    "width": "100%",
                    "height": "100%",
                    "font-size": "12px",
                    "text-valign": "center",
                    "text-halign": "center",
                }
            },

            # Class selectors
            {
                'selector': '.red',
                'style': {
                    'background-color': [255, 105, 180],
                    'line-color': [255, 105, 180]
                }
            },
            {
                'selector': '.blue',
                'style': {
                    'background-color': [65, 105, 225],
                    'line-color': [65, 105, 225]
                }
            },
            {
                'selector': '.gold',
                'style': {
                    'background-color': [245, 189, 2],
                    'line-color': [245, 189, 2]
                }
            },
            {
                'selector': '.dashed',
                'style': {
                    'line-style': 'dashed'
                }
            },
            {
                'selector': '.solid',
                'style': {
                    'line-style': 'solid'
                }
            } 

        ]
    )
])


if __name__ == "__main__":
    app.run_server(debug=True)
