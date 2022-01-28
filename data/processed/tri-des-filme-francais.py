import pandas as pd
y = 0
x = 0
df = pd.read_csv("merged.csv")
for c,t in zip(df["country"],df["type"]):
    if "France" in str(c):
        x += 1
        print(c)
        if "TV Show" not in str(t) and "Movie" in str(t):
            print(t)
            y += 1
print("Il y a :", y, "film Francais")
