import pandas as pd

x = pd.DataFrame(
    {
        'dt': ['2016-01-01','2016-01-03', '2016-01-04','2016-01-01','2016-01-01','2016-01-04'],
        'amount': [10.0,30.0,40.0,78.0,80.0,82.0], 
        'sub_id': [1,1,1,2,2,2]
    })

print(x)

x.dt = pd.to_datetime(x.dt)

cols = ['dt', 'sub_id']

x2 = pd.concat([
    d.asfreq('D').ffill(downcast='infer')
    for _, d in x.drop_duplicates(cols, keep='last')
                 .set_index('dt').groupby('sub_id')
]).reset_index()

print(x2)