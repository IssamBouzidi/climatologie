class Helper:

    @staticmethod
    def load_data():
        RAW_DIR = '../../data/RAW/'
        fields = ['Region', 'Country', 'City', 'Month', 'Day', 'Year', 'AvgTemperature']

        def logic(index):
            if index % 3 == 0:
                return True
            return False
        
        # Skip rows from based on condition like skip every 3rd line
        
        dataframe = pd.read_csv(os.path.join(RAW_DIR, 'temperatures.csv'), usecols=fields, skiprows= lambda x: logic(x))

    @staticmethod
    def convert_celsius_to_fahrenheit(fahrenheit_value):
        return (fahrenheit_value - 32) / 1.8
        