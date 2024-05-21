a, b = 0, 1
max_int32 = 2**31 - 1

while True:
    c = a + b
    if c >= max_int32:
        break
    a, b = b, c

print(f"32비트 int형에서 표현할 수 있는 최대 피보나치 수는 {b}입니다.")