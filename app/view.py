#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Kairat
"""

import dash_core_components as dcc
import dash_html_components as html
import dash_daq as daq

def get_layout():
    return html.Div(children=[
        html.Div(id='hidden-vars', children=[
            html.Div(id='age-var'),
            html.Div(id='month-var'),
            html.Div(id='day-var'),
            html.Div(id='weekend-var'),
            html.Div(id='sex-var'),
            html.Div(id='neutered-var'),
            html.Div(id='colormix-var'),
            html.Div(id='purebred-var'),
            html.Div(id='time-var'),
            html.Div(id='animal-var')
        ], style={'display':'none'}),
        html.Div(id='container', className='container u-max-full-width', children=[
            html.Div(className='row', children=[
                html.Div(id='control-panel', className='column', children=[
                    html.Div(id='month', className='row', children=[
                        html.Label('MONTH', id='month-label'),
                        html.Div(children=[
                            html.Button('Jan', id='month-1', n_clicks_timestamp='0'),
                            html.Button('Feb', id='month-2', n_clicks_timestamp='0'),
                            html.Button('Mar', id='month-3', n_clicks_timestamp='0'),
                            html.Button('Apr', id='month-4', n_clicks_timestamp='0'),
                            html.Button('May', id='month-5', n_clicks_timestamp='0'),
                            html.Button('Jun', id='month-6', n_clicks_timestamp='0'),
                            html.Button('Jul', id='month-7', n_clicks_timestamp='0'),
                            html.Button('Aug', id='month-8', n_clicks_timestamp='0'),
                            html.Button('Sep', id='month-9', n_clicks_timestamp='0'),
                            html.Button('Oct', id='month-10', n_clicks_timestamp='0'),
                            html.Button('Nov', id='month-11', n_clicks_timestamp='0'),
                            html.Button('Dec', id='month-12', n_clicks_timestamp='0'),
                        ])
                    ]),
                    html.Div(id='day', children=[
                        html.Label('DAY', id='day-label'),
                        html.Div(children=[
                            html.Button('Mon', id='day-1', n_clicks_timestamp='0'),
                            html.Button('Tue', id='day-2', n_clicks_timestamp='0'),
                            html.Button('Wed', id='day-3', n_clicks_timestamp='0'),
                            html.Button('Thu', id='day-4', n_clicks_timestamp='0'),
                            html.Button('Fri', id='day-5', n_clicks_timestamp='0'),
                            html.Button('Sat', id='day-6', n_clicks_timestamp='0'),
                            html.Button('Sun', id='day-7', n_clicks_timestamp='0')
                        ])
                    ]),
                    html.Div(id='time', children=[
                        html.Label('TIME', id='time-label'),
                        dcc.Slider(id='time-slider',
                            min=0,
                            max=23,
                            marks={
                                0: {'label': 'Midnight'},
                                1: {'label': ''},
                                2: {'label': ''},
                                3: {'label': '3 AM'},
                                4: {'label': ''},
                                5: {'label': ''},
                                6: {'label': '6 AM'},
                                7: {'label': ''},
                                8: {'label': ''},
                                9: {'label': '9 AM'},
                                10: {'label': ''},
                                11: {'label': ''},
                                12: {'label': 'Noon'},
                                13: {'label': ''},
                                14: {'label': ''},
                                15: {'label': '3 PM'},
                                16: {'label': ''},
                                17: {'label': ''},
                                18: {'label': '6 PM'},
                                19: {'label': ''},
                                20: {'label': ''},
                                21: {'label': '9 PM'},
                                22: {'label': ''},
                                23: {'label': ''},
                            },
                            step=1,
                            value=12,
                            updatemode='drag'
                        ),
                    ]),
                    html.Div(className='row', children=[
                        html.Div(id='sex', className='four columns', children=[
                            html.Div(id='female', className='six columns', children=[
                                html.Div(id='sex-1', n_clicks_timestamp='0', children=[]),
                                html.Div('Female', id='female-label', className='sex-option-label')
                            ]),
                            html.Div(id='male', className='six columns', children=[
                                html.Div(id='sex-2', n_clicks_timestamp='0', children=[]),
                                html.Div('Male', id='male-label', className='sex-option-label')
                            ]),
                        ]),
                        html.Div(className='eight columns', children=[
                            html.Div(id='neutered', className='four columns', children=[
                                daq.BooleanSwitch(
                                    id='neutered-switch',
                                    on=True,
                                    label={'label': "NEUTERED?", 'style': {'font-size': '11px', 
                                                                           'font-weight': 600, 
                                                                           'letter-spacing': '.1rem'}},
                                    labelPosition="top"
                                )
                            ]),
                            html.Div(id='colormix', className='four columns', children=[
                                daq.BooleanSwitch(
                                    id='colormix-switch',
                                    on=True,
                                    label={'label': "MULTICOLOR?", 'style': {'font-size': '11px', 
                                                                           'font-weight': 600, 
                                                                           'letter-spacing': '.1rem'}},
                                    labelPosition="top"
                                )
                            ]),
                            html.Div(id='purebred', className='four columns', children=[
                                daq.BooleanSwitch(
                                    id='purebred-switch',
                                    on=True,
                                    label={'label': "PUREBRED?", 'style': {'font-size': '11px', 
                                                                           'font-weight': 600, 
                                                                           'letter-spacing': '.1rem'}},
                                    labelPosition="top"
                                )
                            ]),
                        ])
                    ]),
                    html.Div(id='age', children=[
                        html.Div(id='age-display', className='row', children=[
                            html.Label('AGE', id='age-label'),
                            html.Span(id='age-weeks-number'),
                            html.Span(id='age-weeks-unit')
                        ]),
                        html.Div(id='age-controller', className='row', children=[
                            html.Div(id='newborn', className='two columns', children=[
                                html.Img(id='newborn-img', width='100%')
                            ]),
                            html.Div(id='age-slider-div', className='seven columns', children=[
                                dcc.Slider(id='age-slider',
                                    min=0,
                                    max=783,
                                    marks={
                                        0: {'label': '0 yrs'},
                                        52: {'label': ''},
                                        104: {'label': ''},
                                        156: {'label': ''},
                                        209: {'label': ''},
                                        261: {'label': '5 yrs'},
                                        313: {'label': ''},
                                        365: {'label': ''},
                                        417: {'label': ''},
                                        469: {'label': ''},
                                        521: {'label': '10 yrs'},
                                        574: {'label': ''},
                                        626: {'label': ''},
                                        678: {'label': ''},
                                        730: {'label': ''},
                                        783: {'label': '15 yrs'}
                                    },
                                    step=1,
                                    value=0,
                                    updatemode='drag'
                                ),
                            ]),
                            html.Div(id='oldie', className='three columns', children=[
                                html.Img(id='oldie-img', width='100%')
                            ])        
                        ])
                    ]),
                    html.Div(id='animal', className='row', children=[
                        html.Div(className='animal-opt six columns', children=[
                            html.Div(id='animal-1', n_clicks_timestamp='0')
                        ]),
                        html.Div(className='animal-opt six columns', children=[
                            html.Div(id='animal-2', n_clicks_timestamp='0')
                        ])
                    ]),
                ]),
                html.Div(id='plot', className='column', children=[
                    html.Div(
                        dcc.Graph(
                            id='outcome-plot'
                        )
                    ),                
                ])
            ])
        ])
    ])