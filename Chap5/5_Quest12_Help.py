def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]

def three_sort(arr, front, mid, rear): #배열, 시작 인덱스, 중앙 인덱스, 마지막 인덱스를 넘겨 받는다.
    if arr[front] > arr[mid]:          #시작 인덱스 값이 중앙 인덱스 값보다 크면 서로 자리를 바꾼다.
        swap(arr, front, mid)
    if arr[mid] > arr[rear]:           #중간 인덱스 값이 마지막 인덱스 값보다 크면 서로 자리를 바꾼다.
        swap(arr, mid, rear)
    if arr[front] > arr[mid]:          #마지막 인덱스 값과 바뀐 중간 인덱스 값의 경우를 대비해 다시 비교한다.
        swap(arr, front, mid)          #시작 인덱스 값이 중앙 인덱스 값보다 크면 서로 자리를 바꾼다.

def mot_qsort(arr, front, rear):
    if rear - front + 1 > 3:                #인덱스가 3개 이상일 때 돌아가는 조건문 작성
        mid = front + (rear - front) // 2   #처음 + (끝-처음) // 2
        three_sort(arr, front, mid, rear)
        
        pivot = arr[mid]
        swap(arr, mid, rear - 1)
        i, j = front, rear - 1
        
        while True:
            while arr[i] < pivot and i < rear:
                i += 1
            while arr[j] > pivot and front < j:
                j -= 1
            if i >= j:
                break
            swap(arr, i, j)
        
        swap(arr, i, rear - 1)
        mot_qsort(arr, front, i - 1)
        mot_qsort(arr, i + 1, rear)

# 테스트용 코드
data = [5, 3, 8, 4, 9, 1, 6, 2, 7]
print("Original : ", data)
mot_qsort(data, 0, len(data)-1)
print("QuickSort : ", data)