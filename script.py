# import pandas as pd
# p=pd.read_csv("C:\Users\srika\OneDrive\Documents\combats.csv")
# #print(p["Winner"])#prints only the column u want
# #print(dict(p.iloc[0:4:2]))#iloc gives th rows and can be converted to a dic
# #if u want to iterate through rows then aways use .iterrows()
# #could use column["the naem of the row"]
# print(p.loc[p["Winner"]==732])#imp
# #        First_pokemon  Second_pokemon  Winner
# # 92               514             732     732
# # 179              385             732     732
# # 442              732               1     732
# # 532              672             732     732
# # 716              703             732     732
# # ...              ...             ...     ...
# # 48651            318             732     732
# # 49164            445             732     732
# # 49241            545             732     732
# # 49763            765             732     732
# # 49978            732             214     732
# print(p.sort_values("First_pokemon",ascending=True))#sorting the value given the row
import pandas as pd
p=pd.read_csv(r"C:\Users\srika\Downloads\PYTHON.py\pokemon2.csv")
print(p.iloc[0,2])


