import pandas as pd

x = pd.DataFrame(
        {
            'city': ['Rabat','Rabat','Rabat','Rabat','Rabat','Rabat','Rabat','Rabat','Paris','Paris'],
            'mois': [1,1,1,1,1,2,2,2,1,1],
            'day': [1,2,3,4,5,1,2,3,1,2],
            'amount': [2,-99,2,2,2,4,-99,2,2,-99]
        }
    )

def avg_temp(row):
    temp_df = x[(x['city'] == row.city) & (x['mois'] == row.month) & (x['day'] == row.day) & (x['amount'] > -99)]
    return (temp_df['amount'].mean(), 2)

x.amount[x['amount'] <= -99] = x.apply(avg_temp, axis = 0)

print(x)

# x2 = x[x['amount'] <= -99]
# x.dt = pd.to_datetime(x.dt)

# cols = ['dt', 'city']

# x2 = pd.concat([
#     d.asfreq('D').ffill(downcast='infer')
#     for _, d in x.drop_duplicates(cols, keep='last')
#                  .set_index('dt').groupby('city')
# ]).reset_index()

# print(x2)