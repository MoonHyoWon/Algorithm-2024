#알고리즘 2.4 > 자연수의 제곱 계산 (O(n^2))

def compute_square_C(n) :
    sum = 0
    for i in range(n):
        for j in range(n):
            sum = sum + 1
    return sum

n = int(input("제곱하고 싶은 수를 입력하시오 : "))

print(n, "의 제곱은 ", compute_square_C(n), "입니다.")