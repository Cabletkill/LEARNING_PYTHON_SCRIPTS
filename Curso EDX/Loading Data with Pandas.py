import pandas as pd
csv_path = 'B:\Nova pasta\mnist_test.csv'
df = pd.read_csv(csv_path)

lista=list(df)
print(df)
#print(lista)
#print(df.loc[2:5,'Album'])
#print(df.iloc[2,0])
#print(df.iloc[0,2])
#print(df.iloc[1,3])