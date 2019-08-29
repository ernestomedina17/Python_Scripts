class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BinaryTree(object):
	def __init__(self, root):
		self.root = Node(root)

	def print_tree(self, traversal_type):
		if traversal_type == "preorder":
			return self.preorder_print(self.root, "")
		elif traversal_type == "inorder":
			return self.inorder_print(self.root, "")
		elif traversal_type == "postorder":
			return self.inorder_print(self.root, "")
		else:
			print("Traversal type " + str(traversal_type) + " is not supported")
			return False

	def preorder_print(self, start, traversal):
		""" Root -> Left -> Right"""
		if start:
			traversal += (str(start.value) + "-")
			traversal = self.preorder_print(start.left, traversal)
			traversal = self.preorder_print(start.right, traversal)
		return traversal

	def inorder_print(self, start, traversal):
		""" Left -> Root -> Right"""
		if start:
			traversal = self.inorder_print(start.left, traversal)
			traversal += (str(start.value) + "-")
			traversal = self.inorder_print(start.right, traversal)
		return traversal
    
	def postorder_print(self, start, traversal):
		""" Left -> Root -> Right"""
		if start:
			traversal = self.inorder_print(start.left, traversal)
			traversal = self.inorder_print(start.right, traversal)
			traversal += (str(start.value) + "-")
		return traversal

# Set up tree:
tree = BinaryTree(1)
#tree.root is a Node object which root's value = 1 
#tree.root.left = None
#tree.root.right = None

tree.root.left = Node(2)
tree.root.right = Node(3)

#  1
#  ^
# 2 3

#tree.root.left.left = None
#tree.root.left.right = None
#tree.root.right.left = None
#tree.root.right.left = None

tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)

#    1
#    ^
#  2   3
#  ^   ^
# 4 5 6 7
#		 8

# Binary Tree Traversals 
# Pre-order Traversal = Root, Let, Right 
# 1 > 2 > 4 > 5 > 3 > 6 > 7 > 8 
print("Pre Order Traversal")
print(tree.print_tree("preorder"))

# In-order Traversal = Left, Root, Right 
# 4 > 2 > 5 > 1 > 6 > 3 > 7 > 8 
print("In Order Traversal")
print(tree.print_tree("inorder"))

# Post-order Traversal = Left, Right, Root
# 4 > 5 > 2 > 1 > 6 > 7 > 3 > 8 
print("Post Order Traversal")
print(tree.print_tree("postorder"))

