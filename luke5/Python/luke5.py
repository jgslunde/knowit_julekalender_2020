import numpy as np
import matplotlib.pyplot as plt

with open("../data/rute.txt", "r") as infile:
    steps = infile.readline()
N = len(steps)
coord = np.zeros((N+1, 2), dtype=int)

for i in range(N):
    coord[i+1] = coord[i]
    if steps[i] == "H":
        coord[i+1,0] += 1
    elif steps[i] == "V":
        coord[i+1,0] -= 1
    elif steps[i] == "O":
        coord[i+1,1] += 1
    elif steps[i] == "N":
        coord[i+1,1] -= 1
    else:
        raise ValueError(f"Unknow character {steps[i]} in steps string.")
if not coord[-1] in np.array([[0,1], [1,0], [0,-1], [-1,0]]):
    raise ValueError(f"Final point {coord[-1]} not next to starting point.")

area = 0
for i in range(N):
    area += (coord[i-1,0]*coord[i,1] - coord[i-1,1]*coord[i,0])
area =  area//2
print(area)

plt.plot(*coord.T, color="black")
plt.fill(*coord.T, color="grey")
plt.show()