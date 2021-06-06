import numpy as np
import random
import sys

def error_occur(data: str) -> str:
    tmp = random.randint(0, 14)
    return data[:tmp] + ('0' if data[tmp] == '1' else '1') + data[tmp + 1:]

def hamming_decode(data: str, error = False) -> str:
    if error:
        data = error_occur(data)
    diff = 0
    for i in range(len(data)):
        if data[i] == '1':
            diff ^= i + 1
    if diff != 0:
        diff -= 1
        data = data[:diff] + ('0' if data[diff] == '1' else '1') + data[diff + 1:]
    return data[2] + data[4:7] + data[8:]

if __name__ == "__main__":
    get_std = ''
    for line in sys.stdin:
        for c in line:
            get_std += c
            if len(get_std) == 45:
                buf = ['', '', '']
                for i in range(45):
                    buf[i % 3] += get_std[i]
                output = hamming_decode(buf[0])
                output += hamming_decode(buf[1])
                output += hamming_decode(buf[2])
                print (output, end = '')
                get_std = ''