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
        df_copy = df.copy()

        for index, row in df.iterrows():
             
            # df_temp = df[
            #             (df['City'] == row['City']) 
            #             & (df['Month'] == row['Month']) 
            #             & (df['Day'] == row['Day'])
            #         ]
            # print(df_temp[df_temp['AvgTemperature'] > -99].mean())
            # avg_temp = round(df_temp[df_temp['AvgTemperature'] > -99].mean(), 2)
            # # print(f'hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh {avg_temp} \n')
            
            
            avg_temp = df[
                    (df['City'] == row['City']) &
                    (df['Month'] == row['Month']) &
                    (df['Day'] == row['Day']) &
                    (df['AvgTemperature'] > -99)
                ]
            print(avg_temp['AvgTemperature'].mean())

            if row['AvgTemperature'] <= -99:
                pass
                # df_copy.at[index,'AvgTemperature'] = 0
            
            

        return df_copy