M = 100                     #테이블의 크기
table = [None]*M         #테이블 만들기 : None으로 초기화

#알고리즘 6.9 문자열 탐색키의 해시 함수 계산
def hashFn(key):          #해시 함수
    sum = 0
    for c in key:
        sum = sum + ord(c)
    return sum % M

#알고리즘 6.6 선형 조사법의 삽입 알고리즘
def insert(key, value):
    id = hashFn(key)
    if table[id] == None:
        table[id] = []
    else:
        for i in table[id]:
            if i[0] == key:
                i[1] == value
                return 
    table[id].append([key, value])

#알고리즘 6.7 선형 조사법의 탐색 알고리즘
def search(key):
    id = hashFn(key)
    for i in table[id]:
        if i[0] == key:
            return i[1]
    return None

#알고리즘 6.8 선형 조사법의 삭제 알고리즘
def delete(key):
    id = hashFn(key)
    if table[id] != None:
        for i in range(len(table[id])):
            if table[id][i][0] == key:           #키를 찾았을 경우
                print(f"'{table[id][i][1]}'의 의미를 가진 '{key}' 단어 삭제")
                del table[id][i]      #파이썬의 del 구문을 사용하면 리스트의 특정 위치의 요소를 삭제
                return True           #찾았다고 Ture 반환
    else :
        print(f"{key}은 단어장에 없는 단어입니다.")

def printf():
    for i in range(M):
        if table[i] != None:
            for j in range(len(table[i])):
                print(i, "번째 단어 >>", table[i][j][0], "의 의미 >>", table[i][j][1])

while True:
    str = input("단어장 프로그램 [p출력, i삽입, d삭제, s탐색, q종료] : ")
    if str == 'p':   #출력
        printf()
    if str == 'i':   #삽입
        word = input("추가 단어 입력 >> ")
        mean = input("단어의 뜻 입력 >> ")
        insert(word, mean)
        print(f"'{mean}'의 의미를 가진 '{word}' 단어 추가")

    if str == 'd':   #삭제
        word = input("삭제 단어 입력 >> ")
        delete(word)

    if str == 's':   #탐색
        word = input("탐색 단어 입력 >> ")
        mean = search(word)
        print(f"'{mean}'의 의미를 가진 '{word}' 단어 탐색")

    if str == 'q':   #종료
        break