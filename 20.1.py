#ps: ირაკლი, დავალებაში თავიდან შეცდომით წამეკითხა, countleaf მეგონა edge-ის ნაცვლად, ამიტომ ეგეც დავწერე. დამენანა წასაშლელად.

#pps: ალგორითმები ჩემით მოვიფიქრე, ამიტომ შეიძლება მთლად ოპტიმალური კოდი არ იყოს:)

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return TreeNode(key)
        
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)

        return node
    
    def countLeafNodes(self):
        counter = self._countLeafNodes(self.root, 0, 0)
        return counter

    def _countLeafNodes(self, node, countNodesR, countNodesL): #B) Like a boss

        if node:
            
            if not node.left and not node.right:
                return 1
            
            if node.right:
                countNodesR += self._countLeafNodes(node.right, countNodesR,0)
            if node.left:
                countNodesL += self._countLeafNodes(node.left, 0, countNodesL)
        
        return countNodesR + countNodesL
    
    def printLeafNodes(self):
        if self.root:
            return self._printLeafNodes(self.root, None)
        else:
            return print("The tree is empty.")

    def _printLeafNodes(self, node, parentNode):

        if not parentNode and not node.left and not node.right:
            print(f"Leaf Node:{node.key}")

        elif node:

            if not node.left and not node.right:
               print(f"Leaf Node:{node.key}")
               return parentNode.key
            
            if node.right:
                self._printLeafNodes(node.right, node)
            if node.left:
                self._printLeafNodes(node.left, node)
            
    def countEdges(self):
        if self.root:
            counter = self._countEdges(self.root, 0, 0)
            return counter
        else:
            return 0

    def _countEdges(self, node, countEdgesR, countEdgesL):

        if node:
            
            if not node.left and not node.right:
                return 0
            
            if node.right:
                countEdgesR = self._countEdges(node.right, countEdgesR,0) + 1
            if node.left:
                countEdgesL = self._countEdges(node.left, 0, countEdgesL) + 1
            
        return countEdgesR + countEdgesL
    

binaryTree = BinaryTree()
binaryTree.insert(10)
binaryTree.insert(5)
binaryTree.insert(3)
binaryTree.insert(6)
binaryTree.insert(15)
binaryTree.insert(11)
binaryTree.insert(20)
binaryTree.insert(21)
binaryTree.insert(27)
binaryTree.insert(19)


print(f"Number of leaf nodes: {binaryTree.countLeafNodes()}")

binaryTree.printLeafNodes()

print(f"Number of edges: {binaryTree.countEdges()}")

