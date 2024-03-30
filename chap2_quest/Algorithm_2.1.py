#알고리즘 2.1 > 순차 탐색

A = [32, 14, 5, 17, 23, 9, 11, 4, 26, 29]

def sequential_search(A, key):
    for i in range(len(A)):
        if A[i] == key:
            return 1
        
    return -1

answer = sequential_search(A, 11)
if (answer >= 0):
    print("키 값이 리스트에 있습니다.")
else :
    print("키 값이 리스트에 없습니다.")