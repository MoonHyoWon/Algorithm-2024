# asterisk(5)에서 호출될 때 출력되는 *의 개수는?

def asterisk(i) :
    if i > 1 :
        asterisk(i/2)
        asterisk(i/2)
    print("*", end="")

asterisk(5)