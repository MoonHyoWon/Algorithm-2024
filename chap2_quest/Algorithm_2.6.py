#알고리즘 2.6 > 이진수 변환에서 총 비트 수 계산(반복 알고리즘)

def binary_digits(n) :
    count = 1
    while n > 1:
        count = count + 1
        n = n // 2 #정수 나눗셈
    return count

n = int(input("이진수 비트 수를 알고 싶은 숫자를 입력하시오 : "))

print(n, "이 필요한 이진수 비트의 수는 ", binary_digits(n), "입니다.")