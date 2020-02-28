#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Kairat
"""

from dash.dependencies import Input, Output, State
import numpy as np
import pandas as pd
import base64

import model 

def register_callbacks(app):
        
    # Month
    @app.callback(
        Output('month-var', 'children'),
        [Input('month-1', 'n_clicks_timestamp'),
         Input('month-2', 'n_clicks_timestamp'),
         Input('month-3', 'n_clicks_timestamp'),
         Input('month-4', 'n_clicks_timestamp'),
         Input('month-5', 'n_clicks_timestamp'),
         Input('month-6', 'n_clicks_timestamp'),
         Input('month-7', 'n_clicks_timestamp'),
         Input('month-8', 'n_clicks_timestamp'),
         Input('month-9', 'n_clicks_timestamp'),
         Input('month-10', 'n_clicks_timestamp'),
         Input('month-11', 'n_clicks_timestamp'),
         Input('month-12', 'n_clicks_timestamp')])
    def update_month_var(jan, feb, mar, apr, may, jun,
                         jul, aug, sep, octo, nov, dec):
        months = np.array([jan, feb, mar, apr, may, jun, jul, aug, sep, octo, nov, dec], dtype=int)
        return np.argmax(months) + 1
    
    def register_month_callback(i):
        @app.callback(
            Output('month-{}'.format(i), 'className'),
            [Input('month-var', 'children')])
        def update_month_btn_class(month):
            if month == i:
                return 'selected'
            else:
                return ''
        return update_month_btn_class
    
    for i in range(1,13):
        register_month_callback(i)
        
    # Day
    @app.callback(
        Output('day-var', 'children'),
        [Input('day-1', 'n_clicks_timestamp'),
         Input('day-2', 'n_clicks_timestamp'),
         Input('day-3', 'n_clicks_timestamp'),
         Input('day-4', 'n_clicks_timestamp'),
         Input('day-5', 'n_clicks_timestamp'),
         Input('day-6', 'n_clicks_timestamp'),
         Input('day-7', 'n_clicks_timestamp')])
    def update_day_var(mon, tue, wed, thu, fri, sat, sun):
        days = np.array([mon, tue, wed, thu, fri, sat, sun], dtype=int)
        return np.argmax(days)
    
    def register_day_callback(i):
        @app.callback(
            Output('day-{}'.format(i), 'className'),
            [Input('day-var', 'children')])
        def update_day_btn_class(day):
            if day+1 == i:
                return 'selected'
            else:
                return ''
        return update_day_btn_class
    
    for i in range(1,8):
        register_day_callback(i)
        
        
    # Weekend
    @app.callback(
        Output('weekend-var', 'children'),
        [Input('day-var', 'children')])
    def update_weekend_var(day):
        if day >= 5:
            return 1
        else:
            return 0
    
    # Sex
    @app.callback(
        Output('sex-var', 'children'),
        [Input('sex-1', 'n_clicks_timestamp'),
         Input('sex-2', 'n_clicks_timestamp')])
    def update_sex_var(female, male):
        sexes = np.array([female, male], dtype=int)
        return np.argmax(sexes)
    
    def register_sex_callback(i):
        @app.callback(
            Output('sex-{}'.format(i), 'className'),
            [Input('sex-var', 'children')])
        def update_sex_btn_class(sex):
            if sex+1 == i:
                return 'selected'
            else:
                return ''
        return update_sex_btn_class
    
    for i in range(1,3):
        register_sex_callback(i)
        
        
    # Neutered 
    @app.callback(
        Output('neutered-var', 'children'),
        [Input('neutered-switch', 'on')])
    def update_neutered_var(on):
        return 1 if on else 0
    
    # Mixed color 
    @app.callback(
        Output('colormix-var', 'children'),
        [Input('colormix-switch', 'on')])
    def update_colormix_var(on):
        return 1 if on else 0
    
    # Purebred 
    @app.callback(
        Output('purebred-var', 'children'),
        [Input('purebred-switch', 'on')])
    def update_purebred_var(on):
        return 1 if on else 0
    
    # Time
    @app.callback(
        Output('time-var', 'children'),
        [Input('time-slider', 'value')])
    def update_time_var(hour):
        return hour
    
    # Age
    @app.callback(
        Output('age-var', 'children'),
        [Input('age-slider', 'value')])
    def update_age_var(value):
        return value
    
    @app.callback(
        Output('age-weeks-number', 'children'),
        [Input('age-slider', 'value')])
    def update_age_display(value):
        return value
    
    @app.callback(
        Output('age-weeks-unit', 'children'),
        [Input('age-slider', 'value')])
    def update_age_weeks_unit(value):
        if value == 1:
            return ' week'
        else:
            return ' weeks'
        
    @app.callback(
        Output('newborn-img', 'src'),
        [Input('animal-var', 'children')])
    def update_newborn_pic(animal):
        if animal == 0:
            image_filename = 'img/kitten.png'
            encoded_image = base64.b64encode(open(image_filename, 'rb').read())
            return 'data:image/png;base64,{}'.format(encoded_image.decode())
        else:
            image_filename = 'img/puppy.png'
            encoded_image = base64.b64encode(open(image_filename, 'rb').read())
            return 'data:image/png;base64,{}'.format(encoded_image.decode())
        
    @app.callback(
        Output('oldie-img', 'src'),
        [Input('animal-var', 'children')])
    def update_oldie_pic(animal):
        if animal == 0:
            image_filename = 'img/oldie-cat.png'
            encoded_image = base64.b64encode(open(image_filename, 'rb').read())
            return 'data:image/png;base64,{}'.format(encoded_image.decode())
        else:
            image_filename = 'img/oldie-dog.png'
            encoded_image = base64.b64encode(open(image_filename, 'rb').read())
            return 'data:image/png;base64,{}'.format(encoded_image.decode())
    
    # Animal
    @app.callback(
        Output('animal-var', 'children'),
        [Input('animal-1', 'n_clicks_timestamp'),
         Input('animal-2', 'n_clicks_timestamp')])
    def update_animal_var(cat, dog):
        animals = np.array([cat, dog], dtype=int)
        return np.argmax(animals)
    
    def register_animal_callback(i):
        @app.callback(
            Output('animal-{}'.format(i), 'className'),
            [Input('animal-var', 'children')])
        def update_animal_btn_class(animal):
            if animal+1 == i:
                return 'selected'
            else:
                return ''
        return update_animal_btn_class
    
    for i in range(1,3):
        register_animal_callback(i)

    @app.callback(
        Output('outcome-plot', 'figure'),
        [Input('age-var', 'children'),
         Input('month-var', 'children'),
         Input('day-var', 'children'),
         Input('weekend-var', 'children'),
         Input('sex-var', 'children'),
         Input('neutered-var', 'children'),
         Input('colormix-var', 'children'),
         Input('purebred-var', 'children'),
         Input('time-var', 'children'),
         Input('animal-var', 'children')])        
    def get_plot_figure(age, month, day, weekend, sex, neutered, colormix, purebred, time, animal):
        outcomes = ['Adoption', 'Died', 'Euthanasia', 'Return to owner', 'Transfer']
        columns = ['AgeInWeeks', 'PureBreed', 'ColorMix', 'Weekday', 'Weekend', 'Hour',
                   'Month', 'AnimalType_Dog', 'Neutered_1', 'Neutered_Unknown', 'Sex_1',
                   'Sex_Unknown']
        
        # It's very important to preserve the column order, so that the saved model behaves correctly
        df = pd.DataFrame([[age, purebred, colormix, day, weekend, time, month, animal, neutered, 0, sex, 0]], 
                         columns=columns)
        X = pd.get_dummies(df, drop_first=True)
        y = model.random_forest.predict_proba(X)
    
        return {'data': [
                    {'x': outcomes, 
                     'y': np.ravel(y), 
                     'type': 'bar',
                     'marker': dict(
                        color=['#4ECDC4', '#F76C5E',
                               '#F68E5F', '#586BA4',
                               '#324376']),
                    }
                ],
                'layout': {
                    'title': 'Shelter Animal Outcome Probabilities',
                    'yaxis': dict(
                        title='Probability',
                        titlefont=dict(
                            size=16,
                            color='rgb(107, 107, 107)'
                        ),
                        tickfont=dict(
                            size=14,
                            color='rgb(107, 107, 107)'
                        )
                    ),
                    'xaxis': dict(
                        tickfont=dict(
                            color='rgb(107, 107, 107)'
                        )
                    ),
                },
            }