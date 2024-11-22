# file = open('example.csv', 'r')
#
# lines = file.readlines()
#
# for line in lines:
#     print(line)
#     elements = line.split(',')

import pandas as pd

# df = data frame
df = pd.read_csv('example.csv')
# print(df.head())
# print(df.shape)
# print(df.index)
# print(df.columns)

# print(df['Name'])
# print(df.loc[0, 2])
print(df.iloc[1, 0])
print(df.loc[1, 'Name'])

for index, row in df.iterrows():
    print(index)
    print(row)
