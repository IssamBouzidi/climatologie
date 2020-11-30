import pandas as pd
import os
from os import path

class Helper:

    @staticmethod
    def load_data(year_begin = 1995, year_end=2020):
        RAW_DIR = '../data/RAW/'
        fields = ['Region', 'Country', 'City', 'Month', 'Day', 'Year', 'AvgTemperature']
        
        # Skip rows from based on condition like skip every 3rd line
        
        dataframe = pd.read_csv(os.path.join(RAW_DIR, 'temperatures.csv'), usecols=fields)

        return dataframe.loc[dataframe['Year'] in range(1995, 2019)]

    @staticmethod
    def convert_celsius_to_fahrenheit(fahrenheit_value):
        return (fahrenheit_value - 32) / 1.8
        