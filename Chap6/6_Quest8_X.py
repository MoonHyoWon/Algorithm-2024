def counting_sort(A, N):
    output = [0] * len(A)
    count = [0] * MAX_VAL

    for i in range(len(N)):
        for j in range(len(A)):
            if A[j] == N[i]:
                count[i] += 1
    
    for i in range(MAX_VAL):
        count[i] += count[i-1]
    
    for i in range(len(A)):
        output[count[A[i]-1]] = A[i]
        count[A[i]] -= 1
    
    for i in range(len(A)):
        A[i] = output[i]

MAX_VAL = 15
data = [ '고', '고', '즘', '알', '리', '알', '즘', '즘', '고', '리' ]
name = ['알', '고', '리', '즘']
print("Original : ", data)
counting_sort(data, name)
print("Counting : ", data)
