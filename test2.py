import pandas as pd
import glob

path = r'C:\Users\sarah\Desktop\cours\sae\sae 15'
all_files = glob.glob(path + "netflix-1.csv"+"netflix-2.csv"+"netflix-3.csv"+"netflix-4.csv"+"netflix-5.csv")

li = []

for filename in all_files:
    df = pd.read_csv(filename, index_col=None, header=0)
    li.append(df)

frame = pd.concat(li, axis=0, ignore_index=True)