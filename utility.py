# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 22:30:29 2020

@author: Khare
"""
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score
from math import sqrt

def evaluate_model(forecast, actual):
    mape = np.mean(np.abs(forecast-actual)/np.abs(actual))
    mpe = np.mean((forecast - actual)/actual)
    rms = np.sqrt(mean_squared_error(forecast, actual))
    print("Evaluation Metrics:")
    print('--------------------')
    print('RMS:{}'.format(rms))
    print('MAPE:{}'.format(mape))
    print('MPE:{}'.format(mpe))
    print('--------------------')  