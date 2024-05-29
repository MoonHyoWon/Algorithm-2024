def counting_sort(A, N):
    output = [0] * len(A)
    count = [0] * len(N)
    
    for char in A:
        count[N.index(char)] += 1
    
    for i in range(1, len(N)):
        count[i] += count[i-1]
    
    for char in reversed(A):
        index = N.index(char)
        count[index] -= 1
        output[count[index]] = char
    
    for i in range(len(A)):
        A[i] = output[i]

name = ['알', '고', '리', '즘']
name.sort()  # 사전순으로 정렬
data = ['고', '고', '즘', '알', '리', '알', '즘', '즘', '고', '리']

print("Original:", data)
counting_sort(data, name)
print("Counting:", data)