#알고리즘 2.7 > 순환적인 팩토리얼 알고리즘

def factorial(n):
    if n == 1:
        return 1
    else :
        return n * factorial(n-1)

n = int(input("팩토리얼 문제를 계산할 정수를 입력하시오 : "))
print(n, "의 팩토리얼은 ", factorial(n), "입니다.")