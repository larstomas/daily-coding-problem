
class Node:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right


def serialize(root):
	if root is None:
		return '#'
	serialize_left = serialize(root.left)
	serialize_right = serialize(root.right)
	serialized = '{},{},{}'.format(root.val, serialize_left, serialize_right)
	return serialized
# alt   return '{} {} {}'.format(root.val, serialize(root.left), serialize(root.right))


def deserialize(data):
	def helper():
		val = next(vals)
		if val == '#':
			return None
		node = Node(str(val))
		node.left = helper()
		node.right = helper()
		return node
	vals = iter(data.split(','))
	return helper()

# Inpot node
node = Node('root', Node('left', Node('left.left')), Node('right'))
s = 'root,left,left.left,X,X,X,right,X,X'

# print(serialize(node))

assert deserialize(serialize(node)).left.left.val == 'left.left'
