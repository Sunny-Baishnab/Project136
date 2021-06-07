import pandas as pd
import csv

df = []
with open('f.csv') as f:
    reader = csv.reader(f)
    for i in reader:
        df.append(i)

data_rows = df[1:]

final_star_list = []

for i in data_rows:
    temp_dict = {
      'Name':i[1],
      'Distance':i[2],
      'Mass':i[3],
      'Radius':i[4],
      'Gravity':i[5]
    }

    final_star_list.append(temp_dict)

print(final_star_list)