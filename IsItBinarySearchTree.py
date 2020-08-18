class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def checkBST(root):
    if root == None:
        return True
    if checkRight(root.right, root.data) and checkLeft(root.left, root.data) and checkBST(root.left) and checkBST(root.right):
        return True
    else:
        return False


def checkRight(root, data):
    if root == None:
        return True
    if root.data > data and checkRight(root.left, data) and checkRight(root.right, data):
        return True
    else:
        return False


def checkLeft(root, data):
    if root == None:
        return True
    if root.data < data and checkLeft(root.left, data) and checkLeft(root.right, data):
        return True
    else:
        return False
