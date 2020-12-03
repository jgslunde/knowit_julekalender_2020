import numpy as np
from tqdm import trange

Nmatrix = 1000

matrix = np.zeros((Nmatrix, Nmatrix), dtype=np.uint8)

with open("../data/matrix.txt", "r") as infile:
    for i, line in enumerate(infile):
        matrix[i] = np.array([ord(line[i]) for i in range(Nmatrix)])

words = []
with open("../data/wordlist.txt", "r") as infile:
    for i, line in enumerate(infile):
        line = line.split("\n")[0]
        words.append(np.array([ord(line[i]) for i in range(len(line))], dtype=np.uint8))

words_string = np.loadtxt("../data/wordlist.txt", dtype=str)

found_words = np.zeros(len(words), dtype=bool)

for i in trange(Nmatrix):
    for j in range(Nmatrix):
        for k, word in enumerate(words):
            N = len(word)

            if i + N <= Nmatrix:
                if (matrix[i:i+N,j] == word).all():
                    print("Found:", words_string[k], "at", i, j)
                    found_words[k] = True
                if (matrix[i:i+N:,j] == word[::-1]).all():
                    print("Found:", words_string[k], "at", i, j)
                    found_words[k] = True
            if j + N <= Nmatrix:
                if (matrix[i,j:j+N] == word).all():
                    print("Found:", words_string[k], "at", i, j)
                    found_words[k] = True

                if (matrix[i,j:j+N] == word[::-1]).all():
                    print("Found:", words_string[k], "at", i, j)
                    found_words[k] = True
for offset in trange(-Nmatrix, Nmatrix+1):
    diagonal = np.diagonal(matrix, offset=offset)
    M = len(diagonal)
    for i in range(M):
        for k, word in enumerate(words):
            N = len(word)

            if i + N <= M:
                if (diagonal[i:i+N] == word).all():
                    print("Found:", words_string[k], "at", i)
                    found_words[k] = True
                if (diagonal[i:i+N] == word[::-1]).all():
                    print("Found:", words_string[k], "at", i)
                    found_words[k] = True

matrix_rot = np.fliplr(matrix)
for offset in trange(-Nmatrix, Nmatrix+1):
    diagonal = np.diagonal(matrix_rot, offset=offset)
    M = len(diagonal)
    for i in range(M):
        for k, word in enumerate(words):
            N = len(word)

            if i + N <= M:
                if (diagonal[i:i+N] == word).all():
                    print("Found:", words_string[k], "at", i)
                    found_words[k] = True
                if (diagonal[i:i+N] == word[::-1]).all():
                    print("Found:", words_string[k], "at", i)
                    found_words[k] = True

print(words_string[~found_words])