import pandas as pd

x = pd.DataFrame(
        {
            'city': ['Rabat','Rabat','Rabat','Rabat','Rabat','Rabat','Rabat','Rabat','Paris','Paris'],
            'mois': [1,1,1,1,1,2,2,2,1,1],
            'day': [1,1,1,4,4,4,2,2,1,1],
            'amount': [2,-99,4,2,2,4,-99,2,2,-99]
        }
    )
# print(x)
def avg_temp(row):
    if row.amount <= - 99:
        # print(row.city)
        temp_df = x[
            (x['city'] == row.city) & 
            (x['mois'] == row.mois) & 
            (x['day'] == row.day) & 
            (x['amount'] > -99)]

        # print(temp_df)
        return round(temp_df['amount'].mean(), 2)
    return row.amount

x2 = x.copy()

print(x2)

# x2.loc[
#     (x['amount'] <= -99) & 
#     (x['city'] == x.city) & 
#     (x['day'] == x.day) & 
#     (x['mois'] == x.mois),'amount'] = 

x2.loc[(x['amount'] <= -99),'amount'] = 0 

# x2.amount[x2['amount'] <= -99] = x.amount[
#             (x['city'] == x2.city) & 
#             (x['mois'] == x2.mois) & 
#             (x['day'] == x2.day) & 
#             (x['amount'] > -99)]


print(x2)
# x2['amount'] = x2.apply(avg_temp, axis=1)
# x = x[x.amount > -99]

# result = pd.concat([x,x2])
# print(result.sort_index())

# x2 = x[x['amount'] <= -99]
# x.dt = pd.to_datetime(x.dt)

# cols = ['dt', 'city']

# x2 = pd.concat([
#     d.asfreq('D').ffill(downcast='infer')
#     for _, d in x.drop_duplicates(cols, keep='last')
#                  .set_index('dt').groupby('city')
# ]).reset_index()

# print(x2)