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
    def preprocessing(df):
        

    @staticmethod
    def convert_celsius_to_fahrenheit(fahrenheit_value):
        return (fahrenheit_value - 32) / 1.8
    
    @staticmethod
    def change_wrong_temperature_value(df):
        df_copy = df.copy()

        for index, row in df.iterrows():            
            df_temp = df[
                    (df['City'] == row['City']) &
                    (df['Month'] == row['Month']) &
                    (df['Day'] == row['Day']) &
                    (df['AvgTemperature'] > -99)
                ]
            avg_temp = round(df_temp['AvgTemperature'].mean(), 2)

            if row['AvgTemperature'] <= -99:
                df_copy.at[index,'AvgTemperature'] = avg_temp       

        return df_copy


    @staticmethod
    def get_avg_temperature(df, city, month, day):
        df_temp = df[(df['City'] == city) & (df['Month'] == month)  & (df['Day'] == day) & (df['AvgTemperature'] >= -99)]
        avg_temp = round(df_temp.mean(), 2)

        return avg_temp


    @staticmethod
    def remove_rows_for_wrong_temperature(df):

        df_to_update = df[df['AvgTemperature'] <= -99]

        for index, row in df_to_update.iterrows():
            temp_df = df[(df['City'] == city) & (df['Month'] == month)  & (df['Day'] == day) & (df['AvgTemperature'] >= -99)]
            df_to_update['AvgTemperature'] = round(temp_df.mean(), 2)
        
        return df_to_update