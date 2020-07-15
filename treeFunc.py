class Node(object):
    def __init__(self, val=-1):
        self.val = val
        self.left = None
        self.right = None


class Tree(object):
    def __init__(self):
        self.root = Node()

    def isEmpty(self):
        if self.root is None:
            return True
        else:
            return False

    def addNode(self, val):
        newNode = Node(val)
        if self.root.val == -1:
            self.root = newNode
        else:
            queue = [self.root]
            while queue:
                node = queue.pop(0)
                if node.left is None:
                    node.left = newNode
                    return
                elif node.right is None:
                    node.right = newNode
                    return
                else:
                    queue.append(node.left)
                    queue.append(node.right)

    def getParent(self, val):
        if self.root.val == val:
            print('根节点无父母')
            return
        tmp = [self.root]
        while tmp:
            node = tmp.pop(0)
            if node.left and node.left.val == val:
                print(node.val)
                return
            if node.right and node.right.val == val:
                print(node.val)
                return
            if node.left is not None:
                tmp.append(node.left)
            if node.right is not None:
                tmp.append(node.right)
        print('树中无该节点')
        return

    def preOrder(self, node):
        if node is None or node.val == -1:
            return
        print(node.val)
        self.preOrder(node.left)
        self.preOrder(node.right)

    def inOrder(self, node):
        if node is None or node.val == -1:
            return
        self.inOrder(node.left)
        print(node.val)
        self.inOrder(node.right)

    def postOrder(self, node):
        if node is None or node.val == -1:
            return
        self.postOrder(node.left)
        self.postOrder(node.right)
        print(node.val)

    def getHeight(self, node):
        if node is None or node.val == -1:
            return 0
        else:
            return max(self.getHeight(node.left), self.getHeight(node.right)) + 1

    def isBalance(self, node):
        if node is None or node.val == -1:
            return True
        leftHeight = self.getHeight(node.left)
        rightHeight = self.getHeight(node.right)
        if abs(leftHeight-rightHeight) > 1:
            return False
        return self.isBalance(node.left) and self.isBalance(node.right)

    def BFSTree(self):
        if self.root is None:
            return []
        result = []
        queue = [self.root]
        while queue:
            popNode = queue.pop(0)
            result.append(popNode.val)
            if popNode.left is not None and popNode.left.val != -1:
                queue.append(popNode.left)
            if popNode.right is not None and popNode.right.val != -1:
                queue.append(popNode.right)
        return result


if __name__ == '__main__':
    tree = Tree()
    treeVal = [1, 2, 3, -1, 4, 5, 6, -1, -1, 7]
    for i in treeVal:
        tree.addNode(i)
    # 树的DFS的三种方式：preOrder,inOrder,postOrder
    # tree.preOrder(tree.root)
    # tree.inOrder(tree.root)
    # tree.postOrder(tree.root)
    # tree.getParent(7)
    # print(tree.getHeight(tree.root))
    # print(tree.isBalance(tree.root))
    # 树的BFS
    print(tree.BFSTree())