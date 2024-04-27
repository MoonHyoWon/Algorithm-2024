def median_of_three(A, left, right):
    midd = (left + right) // 2                 #시작지점 + 끝지점을 2로 나눈 값(중간지점)
    if A[left] > A[midd]:
        A[left], A[midd] = A[midd], A[left]
    if A[left] > A[right]:
        A[left], A[right] = A[right], A[left]
    if A[midd] > A[right]:
        A[midd], A[right] = A[right], A[midd]
    return midd

def quick_sort(A, left, right):
    if left < right:
        mid = partition(A, left, right)
        quick_sort(A, left, mid - 1)
        quick_sort(A, mid + 1, right)

def partition(A, left, right):
    # median_of_three 함수를 사용하여 중간값 피벗 설정
    mid = median_of_three(A, left, right)
    pivot = A[mid]
    A[mid], A[right] = A[right], A[mid]
    
    low = left
    for high in range(left, right):
        if A[high] <= pivot:
            A[low], A[high] = A[high], A[low]
            low += 1
    A[low], A[right] = A[right], A[low]
    return low

data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("Original : ", data)
quick_sort(data, 0, len(data) - 1)
print("QuickSort : ", data)