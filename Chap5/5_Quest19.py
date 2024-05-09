#5장 229p 19번 > 다음의 이진트리를 후위 순회한 결과를 적어라.
class TNode:
    def __init__ (self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

#예제 5.7 이진트리의 후위 순회
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')

a = TNode('A', None, None)
b = TNode('B', None, None)
divi = TNode('/', a, b)
c = TNode('C', None, None)
mult1 = TNode('*', divi, c)
d = TNode('D', None, None)
mult2 = TNode('*', mult1, d)
e = TNode('E', None, None)
root = TNode('+', mult2, e)

print("19. 다음의 이진트리를 후위 순회한 결과를 적어라.")
print('   Post-Order (후위 순환) : ', end=" ")
postorder(root)
print()
