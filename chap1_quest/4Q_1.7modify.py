def gcd(a, b) :
    while b != 0:
        print("gcd (", a, ",", b, ")")
        r = a % b
        a = b
        b = r
    print("gcd (", a, ",", b, ")")
    return a

print("60과 28의 최대 공약수 = ", gcd(60,28))