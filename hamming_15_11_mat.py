import numpy as np
import re
import random

H_matrix = np.mat([
    [1 , 0 , 1 , 0 , 1 , 0 , 1 , 0 , 1 , 0 , 1 , 0 , 1 , 0 , 1],
    [0 , 1 , 1 , 0 , 0 , 1 , 1 , 0 , 0 , 1 , 1 , 0 , 0 , 1 , 1],
    [0 , 0 , 0 , 1 , 1 , 1 , 1 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 1],
    [0 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1],
])

G_matrix = np.mat([
    [1 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
    [1 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
    [0 , 1 , 0 , 1 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
    [1 , 1 , 0 , 1 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
    [1 , 0 , 0 , 0 , 0 , 0 , 0 , 1 , 1 , 0 , 0 , 0 , 0 , 0 , 0],
    [0 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 1 , 0 , 0 , 0 , 0 , 0],
    [1 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0 , 0 , 1 , 0 , 0 , 0 , 0],
    [0 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0],
    [1 , 0 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 1 , 0 , 0],
    [0 , 1 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 1 , 0],
    [1 , 1 , 0 , 1 , 0 , 0 , 0 , 1 , 0 , 0 , 0 , 0 , 0 , 0 , 1]
])

def hamming_encode(data: str) -> str:
    d = []
    for x in data:
        d.append(int(x))
    res = (np.mat(d) * G_matrix) % 2
    return re.sub(r'[^0-1]', '', str(res))
    # return str(res).replace(' ', '').replace('[', '').replace(']', '')

def error_occur(data: str) -> str:
    tmp = random.randint(0, 14)
    return data[:tmp] + ('0' if data[tmp] == '1' else '1') + data[tmp + 1:]

def hamming_decode(data: str, error = False) -> str:
    if error:
        data = error_occur(data)
    d = []
    for x in data:
        d.append(int(x))
    diff = (np.mat(d) * H_matrix.T) % 2
    diff = int(re.sub(r'[^0-1]', '', str(diff)[::-1]), 2)
    if diff != 0:
        diff -= 1
        data = data[:diff] + ('0' if data[diff] == '1' else '1') + data[diff + 1:]
    return data[2] + data[4:7] + data[8:]

if __name__ == "__main__":
    file_lines = []
    f = open('lab2_data/hamming_15_11.txt')
    file_lines = f.readlines()
    f.close()
    print (len(file_lines))
    for line in file_lines:
        data = line.split(',')
        data[0], data[1] = data[0].strip(), data[1].strip()
        assert (hamming_encode(data[0]) == data[1])
        assert (hamming_decode(data[1]) == data[0])
        assert (hamming_decode(data[1], True) == data[0])