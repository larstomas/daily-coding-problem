
from time import process_time

def measureTime(method, n, *args):
    start = process_time()
    for _ in range(n):
        method(*args)
    end = process_time()
    return (end - start) / n

### 

# Inpot node
node = Node('root', Node('left', Node('left.left')), Node('right'))


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def serialize(root):
    if not root:
        return None

    left_subtree = serialize()
    right_subtree = serialize()

    return root.val + left_subtree + right_subtree



def deserialize(s):




assert deserialize(serialize(node)).left.left.val == 'left.left'


repetitions = 1

print(array_product_mod(list_of_numbers_1))
print (measureTime(array_product_mod, repetitions, list_of_numbers_1) * 1000, 'ms')


