import glob
import pandas as pd
import os

path="..\..\data\raw\"
all_filenames=glob.glob(os.path.join(path,"*.csv"))
all_filenames.sort()
all_df=[]
print(all_filenames)
df = pd.read_csv(all_filenames[0],sep=',')
del all_filenames[0]
name=list(df.columns.values)
for f in all_filenames:
    df=pd.read_csv(f,sep=',',names=name)
    all_df.append(df)

merged_df =pd.concat(all_df,ignore_index=True,sort=True)
print(merged_df)
merged_df.to_csv("netflix.csv")