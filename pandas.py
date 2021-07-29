import pandas as pd
import json
import collections
df= pd.read_csv("test_2_2.csv")
flag=0
ft=df.head()
jd= pd.read_json('test_2_headder.json')
rows=jd[0].tolist()
for i in range(len(df)):
    
    le=list(df.loc[i])
    if(set(rows).issubset(set(le))):
        flag = 1
        if flag==1:
            print(i)
