import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('FilteredData.csv')

name = df['Star_name'].to_list()
mass = df['Mass'].to_list()
radius = df['Radius'].to_list()
distance = df['Distance'].to_list()
gravity = df['Gravity'].to_list()

plt.bar(name,mass)
plt.title("Name & Mass of the star")
plt.xlabel("Name")
plt.ylabel("Mass")
plt.show()

plt.bar(name,radius)
plt.title("Name & Radius of the star")
plt.xlabel("Name")
plt.ylabel("Radius")
plt.show()

plt.bar(name,distance)
plt.title("Name & Distance of the star")
plt.xlabel("Name")
plt.ylabel("Distance")
plt.show()

plt.bar(name,gravity)
plt.title("Name & Gravity of the star")
plt.xlabel("Name")
plt.ylabel("Gravity")
plt.show()