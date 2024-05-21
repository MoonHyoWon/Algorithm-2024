import time

#알고리즘 5.12 피보나치수열(분할정복) [순환구조]                                  #시간복잡도 : O(2^n)
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else : 
        return fib(n-1) + fib(n-2)
    

#알고리즘 5.13 피보나치수열(반복구조) [반복구조]                                  #시간복잡도 : O(n)
def fib_iter(n):
    if (n<2): return n
    last = 0
    current = 1
    for i in range(2, n+1):
        tmp = current
        current += last
        last = tmp
    return current

#알고리즘 5.14 피보나치수열(축소 정복 기법의 행렬 거듭제곱 이용) [행렬 거듭제곱]   #시간복잡도 : O(log n)
def fib_mat(n):
    if n<2:
        return n
    mat = [[1,1], [1,0]]
    result = powerMat(mat, n) #알고리즘 4.9 축소 정복 방식 사용
    return result[0][1]

#알고리즘 4.9 행렬의 거듭제곱(축소 정복 기법)
def powerMat(x, n):
    if n == 1:
        return x
    elif (n%2) == 0:
        return powerMat(multMat(x,x), n//2)
    else:
        return multMat(x, powerMat(multMat(x,x), (n-1) // 2))

def multMat(A, B):
    # 행렬 A의 행과 B의 열의 수를 가져옵니다.
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # A의 열 수와 B의 행 수가 같아야 합니다.
    if cols_A != rows_B:
        raise ValueError("행렬 A의 열 수는 행렬 B의 행 수와 같아야 합니다.")

    # 결과 행렬 C를 초기화합니다.
    C = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # 행렬 곱셈을 수행합니다.
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]

    return C


num = int(input("피보나치수열을 계산할 숫자를 입력하시오 > "))

start_time = time.time()
print("      순환구조 피보나치수열 : ", fib(num))
end_time = time.time()
print(f"      순환구조 실행 시간: {end_time - start_time}초")

start_time = time.time()
print("      반복구조 피보나치수열 : ", fib_iter(num))
end_time = time.time()
print(f"      반복구조 실행 시간: {end_time - start_time}초")

start_time = time.time()
print(" 행렬 거듭제곱 피보나치수열 : ", fib_mat(num))
end_time = time.time()
print(f" 행렬 거듭제곱 실행 시간: {end_time - start_time}초")