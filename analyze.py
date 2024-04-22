import pandas as pd
a=pd.read_csv("google_comments.tsv",sep="\t")
print(a)
b=a["ratings"].mean()
print(b)