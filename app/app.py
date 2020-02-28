#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Kairat
"""

import dash

import controller
import view

ext_css = []

class AnimalShelterDash(dash.Dash):
    def interpolate_index(self, **kwargs):
        return '''
        <!DOCTYPE html>
        <html>
            <head>
                <title>Shelter Animal Outcome Predictor</title>
		{favicon}
                {css}
            </head>
            <body>
                {app_entry}
                {config}
                {scripts}
                {renderer}
            </body>
        </html>
        '''.format(
	    favicon=kwargs['favicon'],
            css=kwargs['css'],
            app_entry=kwargs['app_entry'],
            config=kwargs['config'],
            scripts=kwargs['scripts'],
            renderer=kwargs['renderer'])

app = AnimalShelterDash(__name__)
app.css.config.serve_locally = True
app.scripts.config.serve_locally = True
#app = dash.Dash(__name__)
app.layout = view.get_layout()
            
controller.register_callbacks(app)

if __name__ == '__main__':
    app.run_server()
