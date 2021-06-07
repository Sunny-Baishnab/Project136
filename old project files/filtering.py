import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('star_with_gravity.csv')

distance = []
for i in df.Distance:
    if i<=100:
        distance.append(True)
    else:
        distance.append(False)

isDistance = pd.Series(distance)
print(isDistance.head())

star_distance = df[isDistance]
star_distance.reset_index(inplace=True,drop=True)
print(star_distance.head())
print(star_distance.shape)

gravity = []
for i in star_distance.Gravity:
    if i>=150 and i<=350:
        gravity.append(True)
    else:
        gravity.append(False)

isGravity = pd.Series(gravity)
print(isGravity.head())

filteredData = star_distance[isGravity]
print(filteredData.head())
print(filteredData.shape)

filteredData.reset_index(inplace=True,drop=True)
print(filteredData.head())

filteredData.to_csv('FilteredData.csv')