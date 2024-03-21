""" 24번 우선순위 큐를 이용해 숫자를 정렬하는 프로그램을 구현해 보자, 
숫자로 이루어진 리스트를 입력받아 우선순위 큐에 모두 넣은 다음 순서대로 
하나씩 꺼내서 원래의 리스트에 저장하면 정렬할 수 있다. 우선순위 큐로는 
파이썬의 heapq 모듈을 사용하라(8.6절의 허프만 코드에서 heapq의 사용법을 참고하라). """

import heapq

def sort_with_heapq(num):
    heapq.heapify(num)
    list_num = []
    while num:
        list_num.append(heapq.heappop(num))
    return list_num

list =  []
while 1 :
    index = int(input("리스트 내용 입력 (음수 입력시 중단) >> "))
    if index >= 0 :
        list.append(index)
    else :
        break
    
result = sort_with_heapq(list)
    
print(f"정렬된 결과: {result}")

