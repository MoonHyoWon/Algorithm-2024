M = 13
table = [None] * M
def hashFn(key):
    return key % M

def lp_insert(key):
    id = hashFn(key)
    count = M
    while count > 0 and (table[id] != None):
        id = (id + 1 + M) % M
        count -= 1
    if count > 0:
        table[id] = key
    return 

def lp_search(key):
    id = hashFn(key)
    count = M
    while count > 0:
        if table[id] == None:
            return None
        if table[id] == key:
            return id
        id = (id + 1 + M) % M
        count -= 1
    return None

def lp_delete(key):
    id = hashFn(key)
    count = M
    while count > 0:
        if table[id] == None:
            return
        if table[id] != -1 and table[id] == key:
            table[id] = -1
            return
        id = (id + 1 + M) % M
        count -= 1

print("  최초:", table)
lp_insert(27); print(" 27 삽입: ", table)
lp_insert(130); print("130 삽입: ", table)
print(" 27의 인덱스 탐색: ", lp_search(27))
print("130의 인덱스 탐색: ", lp_search(130))