import pandas as pd
x=0

df = pd.read_csv("fusion-netflix.csv")

fr = ['France','france']

if df['country']==fr:
    x++1
print(x)






