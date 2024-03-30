#알고리즘 2.2 > 자연수의 제곱 계산 (O(1))

def compute_square_A(n) :
    return n*n

n = int(input("제곱하고 싶은 수를 입력하시오 : "))

print(n, "의 제곱은 ", compute_square_A(n), "입니다.")