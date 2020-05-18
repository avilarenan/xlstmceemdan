from scipy.interpolate import CubicSpline
from keras.preprocessing.sequence import TimeseriesGenerator
import numpy as np

class SplineModel():
    def __init__(self,time_series_generator):
        self.name = "SplineModel"
        self.gen = time_series_generator
    
    def predict(self, x_window, verbose=0):
        for j in range(x_window.shape[1]):
            series = x_window[:,j]
            print(f'series = {series}')
            cs = CubicSpline(np.arange(len(series)), series)
            next_value = cs(len(series)+1)

            return next_value
