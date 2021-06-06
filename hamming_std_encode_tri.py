import numpy as np
import sys

def hamming_encode(data: str) -> str:
    data_tmp = '00' + data[0] + '0' + data[1:4] + '0' + data[4:]
    parity = 0
    for i in range(len(data_tmp)):
        if data_tmp[i] == '1':
            parity ^= i + 1
    parity = (bin(parity)[2:].rjust(4, '0'))[::-1]
    return parity[:2] + data[0] + parity[2] + data[1:4] + parity[3] + data[4:]

if __name__ == "__main__":
    get_std = ''
    for line in sys.stdin:
        for c in line:
            get_std += c
            if len(get_std) == 33:
                buf = hamming_encode(get_std[:11]) + hamming_encode(get_std[11:22]) + hamming_encode(get_std[22:])
                output = ''
                for i in range(45):
                    output += buf[(i % 3) * 15 + i // 3]
                print (output, end = '')
                get_std = ''
        