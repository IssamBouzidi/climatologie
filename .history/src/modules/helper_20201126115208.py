import pandas as pd
import os
from os import path

class Helper:

    @staticmethod
    def load_data():
        RAW_DIR = '../data/RAW/'
        fields = ['Region', 'Country', 'City', 'Month', 'Day', 'Year', 'AvgTemperature']

        def logic(Year):
            if Year in range(1995, 2019):
                return False
            return True
        
        # Skip rows from based on condition like skip every 3rd line
        
        dataframe = pd.read_csv(os.path.join(RAW_DIR, 'temperatures.csv'), usecols=fields)

        return dataframe

    @staticmethod
    def convert_celsius_to_fahrenheit(fahrenheit_value):
        return (fahrenheit_value - 32) / 1.8
        