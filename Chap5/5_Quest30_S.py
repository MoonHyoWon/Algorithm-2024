def max_fibonacci(): 
    max_int = 2147483647
    a, b = 0, 1
    while b <= max_int - a: 
        a, b = b, a + b 
        return a 
    
max_fib = max_fibonacci() 
print("최대 피보나치 수:", max_fib)