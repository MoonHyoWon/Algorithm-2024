""" 24번 우선순위 큐를 이용해 숫자를 정렬하는 프로그램을 구현해 보자, 
숫자로 이루어진 리스트를 입력받아 우선순위 큐에 모두 넣은 다음 순서대로 
하나씩 꺼내서 원래의 리스트에 저장하면 정렬할 수 있다. 우선순위 큐로는 
파이썬의 heapq 모듈을 사용하라(8.6절의 허프만 코드에서 heapq의 사용법을 참고하라). """

# 허프만 트리 생성 알고리즘
# 파이썬에서의 우선순위 큐

import heapq

def make_heap_tree(freq, label):
    n = len(freq)
    h = []
    for i in range(n):
        heapq.heappush(h, (freq[i], label[i]))

    for i in range(1, n) :
        e1 = heapq.heappop(h)
        e2 = heapq.heappop(h)
        heapq.heappush(h, (e1[0]+e2[0], e1[1]+e2[1]))
        print(e1, "+", e2)

    print(heapq.heappop(h))

label = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
freq = [24, 3, 8, 10, 33, 6, 4, 12]
make_heap_tree(freq, label)

