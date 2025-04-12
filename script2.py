import pandas as pd
p=pd.read_csv(r"C:\Users\srika\OneDrive\Documents\pokemon2.csv")
p['Total']=p.iloc[:,2:5].sum(axis=1)
k=p.sort_values('Total',ascending=False)
k.to_csv("pokemon2.csv")

