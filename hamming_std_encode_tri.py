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
    read = ''
    for line in sys.stdin:
        for c in line:
            read += c
            if len(read) == 33:
                input = ''
                for i in range(33):
                    input += read[(i % 3) * 11 + i // 3]
                print (hamming_encode(input[:11]), end = '')
                print (hamming_encode(input[11:22]), end = '')
                print (hamming_encode(input[22:]), end = '')
                # print (read[:11], read[11:22], read[22:])
                # print (input)
                read = ''
        