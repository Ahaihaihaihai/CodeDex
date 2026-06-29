import numpy as np
egg_carton1 = np.array([
  [0.89, 0.90, 0.83, 0.89, 0.97, 0.98], 
  [0.95, 0.95, 0.89, 0.95, 0.23, 0.99]
])

egg_carton2 = np.array([
  [0.89, 0.95, 0.84, 0.92, 0.94, 0.93], 
  [0.93, 0.95, 0.02, 0.03, 0.23, 0.99]
])

egg_carton3 = np.array([
  [0.83, 0.95, 0.89, 0.54, 0.37, 0.92], 
  [0.98, 0.99, 0.19, 0.23, 0.89, 0.91]
])

freshness = np.array([np.average(egg_carton1), np.average(egg_carton2), np.average(egg_carton3)])
print(f'carton1: {freshness[0]}, carton2: {freshness[1]}, carton3: {freshness[2]}')
index = int(input('Which carton do you want? '))
print(f'Egg Freshness: {freshness[index-1]}')