import pandas as pd

x = pd.DataFrame({'user': ['a','a','b','b'], 'dt': ['2016-01-01','2016-01-02', '2016-01-05','2016-01-06'], 'val': [1,33,2,1]})
print(x)

x['dt'] = pd.to_datetime(x['dt'])

dates = x.set_index('dt').resample('D').asfreq().index

# DatetimeIndex(['2016-01-01', '2016-01-02', '2016-01-03', '2016-01-04',
#                '2016-01-05', '2016-01-06'],
#               dtype='datetime64[ns]', name='dt', freq='D')

users = x['user'].unique()

# array(['a', 'b'], dtype=object)

idx = pd.MultiIndex.from_product((dates, users), names=['dt', 'user'])

# MultiIndex(levels=[[2016-01-01 00:00:00, 2016-01-02 00:00:00, 2016-01-03 00:00:00, 2016-01-04 00:00:00, 2016-01-05 00:00:00, 2016-01-06 00:00:00], ['a', 'b']],
#            labels=[[0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5], [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]],
#            names=['dt', 'user'])

x.set_index(['dt', 'user']).reindex(idx, fill_value=0).reset_index()

print(x)