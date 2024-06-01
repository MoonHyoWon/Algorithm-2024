class HashMap:
    def __init__(self, size=100):
        # 해시 테이블의 크기를 설정하고 빈 버킷 리스트를 초기화
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        # 주어진 키에 대한 해시 값을 계산
        return hash(key) % self.size

    def insert(self, key, value):
        # 키의 해시 값을 계산하여 버킷 위치를 결정
        h = self._hash(key)
        # 해당 버킷의 모든 항목을 검사하여 이미 존재하는 키인지 확인
        for item in self.table[h]:
            if item[0] == key:
                # 키가 이미 존재하면 값을 업데이트하고 함수 종료
                item[1] = value
                return
        # 키가 존재하지 않으면 새로운 키-값 쌍을 버킷에 추가
        self.table[h].append([key, value])

    def search(self, key):
        # 키의 해시 값을 계산하여 버킷 위치를 결정
        h = self._hash(key)
        # 해당 버킷의 모든 항목을 검사하여 키를 검색
        for item in self.table[h]:
            if item[0] == key:
                # 키가 존재하면 값을 반환
                return item[1]
        # 키가 존재하지 않으면 None을 반환
        return None

    def delete(self, key):
        # 키의 해시 값을 계산하여 버킷 위치를 결정
        h = self._hash(key)
        # 해당 버킷의 모든 항목을 검사하여 키를 검색
        for i, item in enumerate(self.table[h]):
            if item[0] == key:
                # 키가 존재하면 해당 항목을 삭제하고 True를 반환
                del self.table[h][i]
                return True
        # 키가 존재하지 않으면 False를 반환
        return False

    def __str__(self):
        # 해시 맵의 내용을 문자열로 반환
        result = []
        for i, bucket in enumerate(self.table):
            if bucket:
                # 비어있지 않은 버킷만 출력에 포함
                result.append(f"Bucket {i}: {bucket}")
        return "\n".join(result)

# 단어장 프로그램
class VocabularyBook:
    def __init__(self):
        # 해시 맵을 사용하여 단어장 초기화
        self.dictionary = HashMap()

    def add_word(self, word, meaning):
        # 단어와 의미를 해시 맵에 추가
        self.dictionary.insert(word, meaning)
        print(f"'{word}'가 단어장에 추가되었습니다.")

    def find_word(self, word):
        # 단어의 의미를 해시 맵에서 검색
        meaning = self.dictionary.search(word)
        if meaning:
            print(f"'{word}'의 의미는 '{meaning}'입니다.")
        else:
            print(f"'{word}'를 단어장에서 찾을 수 없습니다.")

    def remove_word(self, word):
        # 단어를 해시 맵에서 삭제
        if self.dictionary.delete(word):
            print(f"'{word}'가 단어장에서 삭제되었습니다.")
        else:
            print(f"'{word}'를 단어장에서 찾을 수 없습니다.")

    def display(self):
        # 현재 단어장을 출력
        print("현재 단어장:")
        print(self.dictionary)

# 단어장 프로그램 테스트
vocab_book = VocabularyBook()
vocab_book.add_word("apple", "A fruit that grows on trees.")
vocab_book.add_word("banana", "A long yellow fruit.")
vocab_book.add_word("cat", "A small domesticated carnivorous mammal.")
vocab_book.add_word("dog", "A domesticated carnivorous mammal.")
vocab_book.display()

vocab_book.find_word("banana")
vocab_book.remove_word("banana")
vocab_book.find_word("banana")
vocab_book.display()