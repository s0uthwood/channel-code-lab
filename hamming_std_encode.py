import random
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
    input = ''
    for line in sys.stdin:
        for c in line:
            input += c
            if len(input) == 11:
                print (hamming_encode(input), end = '')
                input = ''
                