import numpy as np
from tqdm import trange

N = 5433000
# N = 20

def is_prime(number):
    is_prime = True
    for i in range(number-1, 1, -1):
        if number%i == 0:
            is_prime = False
            break
    return is_prime

i = 0
nr_packages = 0
while i < N:
    if "7" in str(i):
        for j in range(i, 0, -1):
            if is_prime(j):
                nr_skips = j
                i += j + 1
                break
    else:
        nr_packages += 1
        i += 1

print(nr_packages)