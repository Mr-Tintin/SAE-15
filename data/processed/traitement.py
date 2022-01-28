x = 0
df = pd.read_csv("merged.csv")
for c, t in zip(df["release_year"], df["date_added"]):
    a = str(t).split(",")
    tr = (a[1])
    print(c)
    print(tr)
    if int(c) < int(tr):
        x += 1
    print(x)
print("Il y a :", x, "d'erreur")
