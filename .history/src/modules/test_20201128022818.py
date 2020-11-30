import pandas as pd

x = pd.DataFrame({'user': ['a','a','b','b'], 'dt': ['2016-01-01','2016-01-02', '2016-01-05','2016-01-06'], 'val': [1,33,2,1]})
print(x)

x['dt'] = pd.to_datetime(x['dt'])

dates = x.set_index('dt').resample('D').asfreq().index

DatetimeIndex(['2016-01-01', '2016-01-02', '2016-01-03', '2016-01-04',
               '2016-01-05', '2016-01-06'],
              dtype='datetime64[ns]', name='dt', freq='D')

users = x['user'].unique()

array(['a', 'b'], dtype=object)