import pandas as pd
import os
from os import path

class Helper:

    def __init__(self):
        pass

    @staticmethod
    def load_data(year_begin=1995, year_end=2020):
        RAW_DIR = '../data/RAW/'
        fields = ['Region', 'Country', 'City', 'Month', 'Day', 'Year', 'AvgTemperature']

        dataframe = pd.read_csv(os.path.join(RAW_DIR, 'temperatures.csv'), usecols=fields)

        return dataframe[(dataframe['Year'] >= year_begin) & (dataframe['Year'] < year_end)]

    @staticmethod
    def convert_celsius_to_fahrenheit(fahrenheit_value):
        return (fahrenheit_value - 32) / 1.8
    
    @staticmethod
    def change_wrong_temperature_value(df):

        # print(df)
        for index, row in df.iterrows():
            if row['AvgTemperature'] >= -99
            # print(f'{row['City']}, {row['Day']}, {row['Month']}, {row['Year']}, {row['AvgTemperature']}')
            print(row['Day'], row['Month'], row['Year'], row['AvgTemperature'])
            df_t = df_temperatures_drop_duplicate[(df_temperatures_drop_duplicate['City'] == 'Tirana') & (df_temperatures_drop_duplicate['Month'] == 1)  & (df_temperatures_drop_duplicate['Day'] == 1)]