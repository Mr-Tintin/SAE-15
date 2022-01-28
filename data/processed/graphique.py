import pandas as pd
import statistics
import matplotlib.pyplot as plt
a=[]
c=[]
b=[]
x = []
year = []
df = pd.read_csv("netflix.csv")
a = df.iloc[:, [10]]
dic = {}
for i in df["release_year"]:
    dic[i] = []
for d,y in zip(df["duration"],df["release_year"]):
        if "Seasons" and "Season" in str(d):
            #print(d)
            temp = str(d).split(" ")
            dic[y] = dic[y] + [int(temp[0])]
#del dic['release_year']
#for i in x:
 #   temp = i.split(" ")
 #   c.append(int(temp[0]))
temp = []
for i in dic:
    if len(dic[i]) == 0:
        temp.append(i)
for i in temp:
    del dic[i]

def getkeys(dic):
    return dic.keys()

def ComputeMean(col):
    if len(col) != 0:
        mean = statistics.mean(col)
    else:
        mean = 0
    return (mean)

for i in dic:
    b.append(ComputeMean(dic[i]))
    
year = list(getkeys(dic))
year.sort()


plt.style.use('_mpl-gallery')

ypoints = year
xpoints = b
plt.plot(ypoints,xpoints)

plt.show()


    
    



