import pandas as pd
p=pd.read_csv(r"C:\Users\srika\Downloads\PYTHON.py\pokemon2.csv")
k=p.loc[(p['Type']=='Fighting') &(p["Total"]>130)]#always use this $ sign
l=p.loc[p['Total'].int.contains(6)]
print(l)