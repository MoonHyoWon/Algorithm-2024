import struct

c_4_int = (2 ** 31) - 1  # c언어에서의 4바이트 int 크기값
value = c_4_int

packed_value = struct.pack('i', value)  # 크기값을 패킹 시켜서 4바이트로 고정 시켜줌

F = [1, 1]


def Fibonacci():
    i = 0
    temp = 0
    while True:
        if F[i + 1] > c_4_int:
            print("%d 번째의 피보나치의 수: %d, 패킹된 값: %d" % (i + 1, F[i], struct.unpack('i', packed_value)[0]))
            print("오버플로우 발생!")
            temp = F[i] + F[i + 1]
            F.append(temp)
            i += 1
            over = struct.unpack('i', packed_value)[0] + F[i]
            print("%d 번째의 피보나치의 수: %d, 패킹된 값: %d" % (i + 1, over, struct.unpack('i', packed_value)[0]))
            break
        temp = F[i] + F[i + 1]
        F.append(temp)
        i += 1
    return


Fibonacci()