import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
    dcc.Input(id='my-input', value='initial value', type='text'),
    html.Div(id='my-div')
])


@app.callback(
    Output('my-div', 'children'),
    [Input('my-input', 'value')]
)
def update_output_div(input_value):
    return input_value


if __name__ == '__main__':
    app.run_server()
