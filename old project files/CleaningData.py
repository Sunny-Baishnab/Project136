import pandas as pd
import csv

df = pd.read_csv('final_star_data.csv')
print(df)

df.drop(["Unnamed: 0","star_names.1","radius.1","distance.1","mass.1","row_num.1","row_num"], axis = 1 , inplace = True)
print(df)

final_data = df.dropna()
final_data.reset_index(drop = True , inplace = True)

final_data.to_csv("CleanedData.csv")
