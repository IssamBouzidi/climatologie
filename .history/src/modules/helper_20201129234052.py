import pandas as pd
import os
from os import path
from pandas_profiling import ProfileReport

class Helper:

    RAW_DIR = '../data/RAW/'
    RAPPORT_DIR = '../data/rapports/'
    
    
    def __init__(self):
        pass

    
    @staticmethod
    def load_data(year_begin=1995, year_end=2020):
        
        fields = ['Region', 'Country', 'City', 'Month', 'Day', 'Year', 'AvgTemperature']

        dataframe = pd.read_csv(os.path.join(RAW_DIR, 'temperatures.csv'), usecols=fields)

        return dataframe[(dataframe['Year'] >= year_begin) & (dataframe['Year'] < year_end)]
    

    @staticmethod
    def delete_incomplete_year(df):
        # calculer le nombre de jours pour chaque ville et année
        temp_df_count = df_temperatures_copy.groupby(['City','Year']).size()

        # reinitialiser les index
        temp_df_count = temp_df_count.reset_index()
        
        # renomer les colonnes
        temp_df_count.columns = ['City','Year','Count']
        
        # elliminer les villes et années dont le nombre de jours est different de 365 ou 366
        temp_df = temp_df_count[temp_df_count['Count'].isin([365,366])]

        return temp_df


    @staticmethod
    def preprocessing(df_temperatures):

        # faire une copy du dataframe
        df_temperatures_copy = df_temperatures.copy(deep=True)

        # supprimer les doublons
        df_temperatures_copy.drop_duplicates(subset=None, keep="first", inplace=True)

        ###
        # on va supprimer toute ville qui manque des dates
        ###
        temp_df = Helper.delete_incomplete_year(df_temperatures_copy)        
        
        # merger le dataframe temporaire avec le dataframe des temperatures
        df_temperatures_merged = df_temperatures_copy.merge(temp_df, how='right', right_on=['City','Year'], left_on=['City','Year'])
        
        # supprimer la colonne Count
        del df_temperatures_merged['Count']

        ### 
        # modifier la temperature -99 par la moyenne des temperatures de la ville en meme jour et mois
        ###
        # recuperer les enregisgtrement dont la temperature est inferieur ou egal à -99
        df_temperatures_temp_wrong = df_temperatures_merged[df_temperatures_merged['AvgTemperature'] <= -99]

        # recuperer les enregisgtrement dont la temperature est supperieur ou egal à -99
        df_temperatures_temp_write = df_temperatures_merged[df_temperatures_merged['AvgTemperature'] > -99]

        # calculer la temperature moyenne pour chaque ville, mois et jour
        df_temp_1 = df_temperatures_temp_write.groupby(['City', 'Month', 'Day'])['AvgTemperature'].mean()

        # renommer les colonnes
        df_temp_1.columns = ['City','Month','Day','AvgTemperature']

        # reinitialier l'index
        df_temp_11 = df_temp_1.reset_index()

        # merger les enregistrements propres avec les enregistrements modifiés
        df_temp_2 = df_temperatures_temp_wrong.merge(df_temp_11, how='left', right_on=['City', 'Month', 'Day'], left_on=['City', 'Month', 'Day'])
        del df_temp_2['AvgTemperature_x']

        # renomer les colonnes
        df_temp_2.columns = ['Region', 'Country', 'City', 'Month', 'Day', 'Year', 'AvgTemperature']

        # concatenner la liste des villes avec les temperature propre avec la liste des villes dont les temperatures viennent d'être modifiées
        df_temperatures_temp_final = pd.concat([df_temperatures_temp_write, df_temp_2]).sort_index()

        ###
        # convertir du fahrenheit au celsius
        ###
        df_temperatures_temp_final['AvgTemperature'] = df_temperatures_temp_final['AvgTemperature'].apply(Helper.convert_celsius_to_fahrenheit)

        ### 
        # suprimmer les lignes contenant au moins une valeur NaN
        ###
        df_temperatures_final = df_temperatures_temp_final.dropna()

        # supprimer les villes dont les années ne sont pas completes
        temp_df_deleted = Helper.delete_incomplete_year(df_temperatures_final)
        
        return df_temperatures_final

    @staticmethod
    def convert_celsius_to_fahrenheit(fahrenheit_value):
        return round(((fahrenheit_value - 32) / 1.8), 2)
    
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

    
    @staticmethod
    def save_report(df, name_report):
        if not path.exists(os.path.join(Helper.RAPPORT_DIR, f'{name_report}.html')):
            prof = ProfileReport(df)
            prof.to_file(output_file=os.path.join(Helper.RAPPORT_DIR, f'{name_report}.html'))
        else:
            print('File exists !')
