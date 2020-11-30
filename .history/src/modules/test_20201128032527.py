import pandas as pd

x = pd.DataFrame(
        {
            'city': ['Rabat','Rabat','Rabat','Rabat','Rabat','Rabat','Rabat','Rabat','Paris','Paris'],
            'mois': [1,1,1,1,1,2,2,2,1,1],
            'day': [1,2,3,4,5,1,2,3,1,2]
            'amount': [2,-99,2,2,2,4,-99,2,2,-99]
        }
    )

    
print(x)



# x.dt = pd.to_datetime(x.dt)

# cols = ['dt', 'city']

# x2 = pd.concat([
#     d.asfreq('D').ffill(downcast='infer')
#     for _, d in x.drop_duplicates(cols, keep='last')
#                  .set_index('dt').groupby('city')
# ]).reset_index()

# print(x2)