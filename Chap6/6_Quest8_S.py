def counting_sort(arr):
    # 배열의 고유한 원소를 찾기
    unique_elements = list(set(arr))
    # 고유한 원소들을 정렬
    unique_elements.sort()

    # 각 원소에 고유한 정수 값을 매핑
    element_to_index = {element: idx for idx, element in enumerate(unique_elements)}
    index_to_element = {idx: element for idx, element in enumerate(unique_elements)}

    # 필요한 최대값
    MAX_VAL = len(unique_elements)

    # 정렬할 배열의 크기와 같은 출력 배열 생성
    output = [0] * len(arr)
    count = [0] * (MAX_VAL + 1)

    # 각 원소의 빈도를 계산
    for element in arr:
        count[element_to_index[element]] += 1

    # 누적 합 계산
    for i in range(1, MAX_VAL):
        count[i] += count[i - 1]

    # 정렬된 결과를 출력 배열에 저장
    for element in reversed(arr):
        output[count[element_to_index[element]] - 1] = element
        count[element_to_index[element]] -= 1

    # 원래 배열에 정렬된 결과 복사
    for i in range(len(arr)):
        arr[i] = output[i]

# 주어진 배열
A = ["고", "고", "즘", "알", "리", "알", "즘", "즘", "고", "리"]

# 원래 배열 출력
print("Original:", A)

# 카운팅 정렬 함수 호출
counting_sort(A)

# 정렬된 배열 출력
print("Counting:", A)