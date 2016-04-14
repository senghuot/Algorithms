'''

Premise: given a

'''

class Node(object):
    def __init__(self, data):
        self.data = data
        self.count = 0
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = None

    def add(self, data):
        self.root = self.addHelper(self.root, data)

    def addHelper(self, root, data):

        if root == None:
            return Node(data)

        if data <= root.data:
            root.left = self.addHelper(root.left, data)
            root.count += 1
        else:
            root.right = self.addHelper(root.right, data)

        return root

    def get(self, data):
        return self.getHelper(self.root, data)

    def getHelper(self, root, data):

        if root == None:
            return None

        if data == root.data:
            return root.count

        if data <= root.data:
            res = self.getHelper(root.left, data)
            if res == None: return 0
            return res
        else:
            res = self.getHelper(root.right, data)
            if res == None:
                return 0
            return root.count + 1 + res

tree = Tree()
tree.add(5)
tree.add(1)
tree.add(4)
tree.add(4)
tree.add(5)
tree.add(9)
tree.add(7)
tree.add(13)
tree.add(3)

print tree.get(4)