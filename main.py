import os
import time
import numpy as np

DATA_DIR = "./data/"
NPY_PATH = DATA_DIR + "data.npy"

data = np.load(NPY_PATH)
pictures = []

length, row, col = data.shape
for __l in range(length):
    tmp = ""
    for r in range(row):
        for c in range(col):
            if data[__l, r, c] == 0:
                tmp += "██"
            else:
                tmp += " "
        tmp += "\n"
    pictures.append(tmp)

os.system('cls')
for i in range(0, len(pictures)):
    print("\b" + pictures[i], end="")
    time.sleep(0.02)
    os.system('cls')
