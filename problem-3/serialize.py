
from time import process_time
from collections import deque 



def measureTime(method, n, *args):
    start = process_time()
    for _ in range(n):
        method(*args)
    end = process_time()
    return (end - start) / n

### 

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



def serialize(root):
    if not root:
        return 'X'
    left_subtree = serialize(root.left)
    right_subtree = serialize(root.right)
    return root.val + ',' + left_subtree + ',' + right_subtree

def deserialize(s):
    # Initializing a queue 
    nodes_left = deque(s)

 #   return deserialize_helper(s,0)


#def deserialize_helper(s,index)


# Inpot node
node = Node('root', Node('left', Node('left.left')), Node('right'))
s = 'root,left,left.left,X,X,X,right,X,X,'
s_list = s.split(',')

print(serialize(node))


#assert deserialize(serialize(node)).left.left.val == 'left.left'
