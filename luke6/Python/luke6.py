"""
Approach
Add the total number of candy in all boxes. Then move backwards one box at a time, remove the number of candy in that box from the total.
For each box, check if the total number of candy is now divisible by the number of elves.
"""

import numpy as np

num_elves = 127
boxes = np.loadtxt("../data/godteri.txt", delimiter=",", dtype=int)
num_boxes = len(boxes)

tot_candy = np.sum(boxes)
for i in range(num_boxes-1, 0, -1):
    if tot_candy%num_elves == 0:
        candy_per_elf = tot_candy//num_elves
        boxes_to_open = i + 1
        break
    else:
        tot_candy -= boxes[i]

print("Candy per elf:", candy_per_elf)
print("Boxes to open:", boxes_to_open)