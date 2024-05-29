from queue import Queue
def radix_sort(A):
    queues = []
    for i in range(BUCKETS):
        queues.append(Queue())
    n = len(A)
    factor = 1
    for d in range(DIGITS):
        for i in range(n):
            queues[(A[i]//factor) % BUCKETS].put(A[i])
        j = 0
        for b in range(BUCKETS):
            while not queues[b].empty():
                A[j] = queues[b].get()
                j += 1
        factor *= BUCKETS
        print("step", d+1, A)

BUCKETS = 10 #10진법으로 정렬
DIGITS = 3 #최대 4 자릿수
data = [ 10, 123, 56, 636, 992, 119, 234, 76, 82, 345, 567, 432 ]

radix_sort(data)
print("Radix: ", data)