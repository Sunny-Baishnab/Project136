import pandas as pd

data = pd.read_csv('FilteredData.csv')

data.drop(["Unnamed: 0.1","Unnamed: 0"], axis = 1 , inplace = True)
print(data)

df = data.dropna()
df.reset_index(drop = True , inplace = True)
print(df.head())

df.to_csv('f.csv')

# final_star_list = []

# for i in df:
#   temp_dict = {
#       'Name':i['Star_name'],
#       'Distance':i['Distance'],
#       'Mass':i['Mass'],
#       'Radius':i['Radius'],
#       'Gravity':i['Gravity']
#   }

#   final_star_list.append(temp_dict)

# print(final_star_list)