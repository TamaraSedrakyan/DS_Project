#another page, that upload a picture and shows for which skin type the cosmetics is suitable
import dash_core_components as dcc
import dash_html_components as html

layout = html.Div([
    html.H1("Check whether the cosmetics suits you"),
    #the upload button
    html.Div([
        dcc.Upload(
            id='upload-image',
            children=html.Div(
                ['Upload picture'],
                style={
                    "margin-left": "auto",
                    "margin-right": "auto",
                    'text-align': 'center',
                    'display': 'inline-block'
                }
            ),
            style={
                'width': '20%',
                'height': '40px',
                'lineHeight': '60p',
                'borderStyle': 'hidden',
                'borderRadius': '15px',
                'text-align': 'center',
                "boxShadow": "0px 15px 30px -10px grey",
                "margin-left": "auto",
                "margin-right": "auto",
                "transform": "scale(1.5)",

                "background": "c",
                "background": "-moz-radial-gradient(circle, rgba(70,252,177,1) 4%, rgba(63,251,110,1) 95%)",
                "background": "-webkit-radial-gradient(circle, rgba(70,252,177,1) 4%, rgba(63,251,110,1) 95%)",
                "background": "radial-gradient(circle, rgba(70,252,177,1) 4%, rgba(63,251,110,1) 95%)",
                "filter": "progid:DXImageTransform.Microsoft.gradient(startColorstr='#46fcb1',endColorstr='#3ffb6e',GradientType=1)"
            },
            multiple=False
        )
    ])

])

