def medianOfThree(A, left, right):
    if (len(A) < 3):
        return right
    else :
        midd = left + (right - left) // 2 
        if (A[left] > A[midd] and A[left] < A[right]):    # midd < left < right
            A[left], A[midd] = A[midd], A[left]
        elif (A[right] > A[midd] and A[right] < A[left]): # midd < right < left
            A[right], A[midd] = A[midd], A[right]

        elif (A[left] > A[right] and A[left] < A[midd]): # right < left < midd
            A[left], A[right] = A[right], A[left]
        elif (A[midd] > A[right] and A[midd] < A[left]): # right < midd < left
            A[midd], A[right] = A[right], A[midd]

        elif (A[right] > A[left] and A[right] < A[midd]): # left < midd < right
            A[right], A[left] = A[left], A[right]
        elif (A[midd] > A[left] and A[midd] < A[right]): # left < right < midd
            A[midd], A[left] = A[left], A[midd]

        return midd

#코드 4.12 리스트 분할(Hoare Partition)
def partition(A, left, right):
    #pivot = A[left] # A[0] (== 5) (피벗으로 선택)
    mid = medianOfThree(A, left, right) # 중간값 피벗 선택
    pivot = A[mid]
    A[right], A[mid] = A[mid], A[right] # 피벗을 맨 오른쪽으로 이동

    low = left
    high = right - 1

    while low <= high:                           #low와 high가 역전되지 않는 한 반복
        while low <= high and A[low] <= pivot:   #low가 high보다 작거나 같고 A[low]값이 pivot보다 작을 때
            low += 1                             #low에 1을 더해준다.
        while high >= left and A[high] > pivot:  #high가 left보다 크거나 같고 A[high]가 pivot보다 클 때
            high -= 1                            #high에 1을 빼준다.
        if low < high:
            A[low], A[high] = A[high], A[low]    #low가 high보다 작다면 A[low]와 A[high]의 값을 바꾼다.
    
    A[low], A[right] = A[right], A[low] # 피벗 위치 조정
    return low

#코드 5.3 퀵 정렬
def quick_sort(A, left, right):
    if left < right:
        mid = partition(A, left, right)
        quick_sort(A, left, mid-1)
        quick_sort(A, mid + 1, right)

# median of three : 세 가지의 값을 골라서 고른 값 중 중간 값을 피벗으로 선택한다.
# 12. 퀵 정렬에서 불균형 분할을 완화하기 위해 리스트의 왼쪽, 오른쪽, 중간의 3개의 
# 항목 중에서 중간값을 피벗으로 선택하는 방법(median of three)을 구현하라.
# 이를 위해 알고리즘 4.12의 partition()을 수정하라.

data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("Original : ", data)
quick_sort(data, 0, len(data) - 1)
print("QuickSort : ", data)