NO_OF_CHARS = 128
list = ['A', 'C', 'G', 'T']

#알고리즘 6.3 호스풀 알고리즘의 시프트 테이블 만들기
def shift_table(pat):
    m = len(pat)
    tbl = [m]*NO_OF_CHARS

    for i in range(m-1):
        tbl[ord(pat[i])] = m-1-i
    
    for i in range(len(tbl)):
            if(tbl[i] != 10):
                print(chr(i), " = ", tbl[i]) #아스키코드를 문자로 변환해주는 것 : chr
    return tbl

#알고리즘 6.4 호스풀 알고리즘
def search_horspool(T, P):
    m = len(P)
    n = len(T)
    t = shift_table(P)
    i = m - 1
    while(i<=n-1):
        k = 0
        while k <= m-1 and P[m-1-k]==T[i-k]:
            k += 1
        if k == m:
            return i-m+1
        else:
            tc = t[ord(T[i-k])]
            i += (tc-k)
    return -1

print("패턴의 위치 :", search_horspool("TTATAGATCTCGTATTCTTTTATAGATCTCCTATTCTT", "TCCTATTCTT"))