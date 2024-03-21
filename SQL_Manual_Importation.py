import pandas as pd 

df = pd.read_csv("Book_list.csv")

y = []

for i in range(len(df)):
    x = tuple(df.iloc[i])
    y.append(x)

with open("Books.txt", 'w', encoding = 'utf-8') as Book:
    for tuple in y:
        Book.write(str(tuple) + "," + "\n")