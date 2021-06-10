import random

def hamming_encode(data: str) -> str:
    data_tmp = '00' + data[0] + '0' + data[1:4] + '0' + data[4:]
    parity = 0
    for i in range(len(data_tmp)):
        if data_tmp[i] == '1':
            parity ^= i + 1
    parity = (bin(parity)[2:].rjust(4, '0'))[::-1]
    data_tmp = parity[:2] + data[0] + parity[2] + data[1:4] + parity[3] + data[4:]
    return data_tmp + ('0' if parity_check(data_tmp) else '1')

def error_occur(data: str, num) -> str:
    tmp1, tmp2 = random.sample(range(0, 16), 2)
    assert tmp1 != tmp2
    ret = data[:tmp1] + ('0' if data[tmp1] == '1' else '1') + data[tmp1 + 1:]
    if num == 2:
        ret = ret[:tmp2] + ('0' if ret[tmp2] == '1' else '1') + ret[tmp2 + 1:]
    return ret

def parity_check(data):
    count = 0
    for c in data:
        if c == '1':
            count += 1
    return count % 2 == 0

def hamming_decode(data: str, error = 0) -> str:
    if error > 0:
        data = error_occur(data, error)
    diff = 0
    for i in range(15):
        if data[i] == '1':
            diff ^= i + 1
    # print (diff)
    if diff != 0:
        if parity_check(data):
            return False
        else:
            diff -= 1
            data = data[:diff] + ('0' if data[diff] == '1' else '1') + data[diff + 1:]
    data = data[:-1]
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
        # assert (hamming_encode(data[0]) == data[1])
        assert (hamming_decode(hamming_encode(data[0])) == data[0])
        assert (hamming_decode(hamming_encode(data[0]), 1) == data[0])
        assert (hamming_decode(hamming_encode(data[0]), 2) == False)
        