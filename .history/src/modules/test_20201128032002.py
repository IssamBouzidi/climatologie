import pandas as pd

x = pd.DataFrame(
        {
            'city': ['Rabat','Rabat','Rabat','Rabat','Rabat','Rabat','Rabat','Rabat','Paris','Paris'],
            'dt': ['2016-02-01','2016-02-03', '2016-02-04','2016-02-05','2016-02-10','2016-02-11','2016-02-11','2016-02-12','2016-02-20','2016-03-01'],
            'amount': [10,30,40,78,80,82,44,23,43,22]
        }
    )

print(x)

x['amount']

x.dt = pd.to_datetime(x.dt)

cols = ['dt', 'city']

x2 = pd.concat([
    d.asfreq('D').ffill(downcast='infer')
    for _, d in x.drop_duplicates(cols, keep='last')
                 .set_index('dt').groupby('city')
]).reset_index()

print(x2)