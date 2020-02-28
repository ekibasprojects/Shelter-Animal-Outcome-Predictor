#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Kairat
"""

import pandas as pd
from sklearn.externals import joblib

pickle_file = '../model/animal_outcome.pkl'
random_forest = joblib.load(pickle_file)

