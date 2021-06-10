import random

def hamming_encode(data: str) -> str:
    data_tmp = '00' + data[0] + '0' + data[1:4] + '0' + data[4:]
    parity = 0
    for i in range(len(data_tmp)):
        if data_tmp[i] == '1':
            parity ^= i + 1
    parity = (bin(parity)[2:].rjust(4, '0'))[::-1]
    return parity[:2] + data[0] + parity[2] + data[1:4] + parity[3] + data[4:]

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
    file_lines = []
    f = open('lab2_data/hamming_15_11.txt')
    file_lines = f.readlines()
    f.close()
    print (len(file_lines))
    for line in file_lines:
        data = line.split(',')
        data[0], data[1] = data[0].strip(), data[1].strip()
        # print (hamming_encode(data[0]))
        assert (hamming_encode(data[0]) == data[1])
        assert (hamming_decode(data[1]) == data[0])
        assert (hamming_decode(data[1], True) == data[0])