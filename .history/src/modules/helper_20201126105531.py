class Helper:

    @staticmethod
    def load_data():
        def logic(index):
            if index % 3 == 0:
                return True
            return False
        # Skip rows from based on condition like skip every 3rd line
        usersDf = pd.read_csv('users.csv', skiprows= lambda x: logic(x) )

    @staticmethod
    def convert_celsius_to_fahrenheit(fahrenheit_value):
        return (fahrenheit_value - 32) / 1.8
        