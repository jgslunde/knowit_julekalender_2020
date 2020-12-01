import numpy as np

numbers = np.loadtxt("../data/numbers.txt", dtype=int, delimiter=",")
numbers = np.sort(numbers)
diff = numbers[1:] - numbers[:-1]

print(np.where(diff > 1)[0][0] + 2)