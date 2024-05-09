#5장 229p 18번 > 다음의 이진트리에 대하여 질문에 답하라.
class TNode:
    def __init__ (self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

#예제 5.5 이진트리의 전위 순회
def preorder(n):
    if n is not None:
        print(n.data, end=' ')
        preorder(n.left)
        preorder(n.right)

#예제 5.6 이진트리의 중위 순회
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)

#예제 5.7 이진트리의 후위 순회
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')

n1 = TNode('1', None, None)
n3 = TNode('3', None, None)
n2 = TNode('2', n1, n3)
n5 = TNode('5', None, None)
n4 = TNode('4', n2, n5)
n7 = TNode('7', None, None)
n8 = TNode('8', None, None)
n11 = TNode('11', None, None)
n10 = TNode('10', n8, n11)
n9 = TNode('9', n7, n10)
root = TNode('6', n4, n9)

print("18. 다음의 이진트리에 대하여 질문에 답하라.")
print(" (1) 이 트리를 전위 순회한 결과를 적어라.")
print('   Pre-Order (전위 순환) : ', end=" ")
preorder(root)
print()

print(" (2) 이 트리를 중위 순회한 결과를 적어라.")
print('   In-Order (중위 순환) : ', end=" ")
inorder(root)
print()


print(" (3) 이 트리를 후위 순회한 결과를 적어라.")
print('   Post-Order (후위 순환) : ', end=" ")
postorder(root)
print()
