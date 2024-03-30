#알고리즘 2.5 > 리스트의 중복 항목 탐색

A = [32, 14, 5, 17, 23, 9, 11, 14, 26, 29]
B = [13, 6, 8, 7, 12, 25]

def unique_elements(A) :
    n = len(A)
    for i in range(n-1):
        for j in range(i+1, n):
            if A[i] == A[j]:
                return False
    
    return True

print(A, unique_elements(A))
print(B, unique_elements(B))