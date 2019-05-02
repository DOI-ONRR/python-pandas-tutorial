import pandas as pd

file = r'revenue-test.csv'

#Pandas drops leading 0 of FIPS id without this
df = pd.read_csv(file, dtype={'id': 'str'})

#Sums up rate column when multiple entries exist for each id (county, in this case)
df2 = df.groupby(['id', 'state', 'county'])['rate'].sum()
df2 = df2.reset_index()

#Reads file to a new file, omits index from Pandas, and retains header
df2.to_csv('revenue-test-merged.csv', index=False, header=True)
