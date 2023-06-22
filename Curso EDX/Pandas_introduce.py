import pandas as pd
csv_path = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0101EN-SkillsNetwork/labs/Module%204/data/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)

lista=list(df)
print(df)
print(lista)
print(df.loc[2:5,'Album'])
print(df.iloc[2,0])
print(df.iloc[0,2])
print(df.iloc[1,3])
#print(df.loc[1, 'Artist'])
#print(df.loc[0, 'Released'])
#print(df.iloc[0:2, 0:3])
#print(df.loc[0:8, 'Album':'Rating'])


