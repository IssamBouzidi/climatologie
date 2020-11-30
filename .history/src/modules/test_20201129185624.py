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

x2 = x[x['amount'] <= -99]
x3 = x[x['amount'] > -99]

x33 = x3.groupby(['city', 'mois', 'day'])['amount'].mean()
x33.columns = ['city', 'mois', 'day','count']
x333 = x33.reset_index()

def test(row):
    print(row)
    t =  x333[(x333['city'] == row.city) & (x333['day'] == row.day) & (x333['mois'] == row.mois)]
    # return t['amount']
    return t['amount']
print(x2)
x2['amount'] = x2.apply(test, axis=1)
# print(x2)
# print(x3)
print(x2)

# t = x3.groupby(['city', 'mois', 'day'])['amount'].mean()
# t.columns = ['city', 'mois', 'day', 'amount']
# t.reset_index()

# # x2[['amount']] = 
# print(t)
# print(x2)
# print(x3)
# x2['AvgTempTemp'] = 

# x2.loc[
#     (x['amount'] <= -99) & 
#     (x['city'] == x.city) & 
#     (x['day'] == x.day) & 
#     (x['mois'] == x.mois),'amount'] = 

# x2.loc[(x2['amount'] <= -99),'amount'] 
# e = x[x['amount'] > -99].groupby(['city', 'mois', 'day'])['amount'].mean()
# e.reset_index()
# print(e)
# x2.amount[x2['amount'] <= -99] = x.amount[
#             (x['city'] == x2.city) & 
#             (x['mois'] == x2.mois) & 
#             (x['day'] == x2.day) & 
#             (x['amount'] > -99)]


# print(x2)
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