class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

""" 
Full Tree: every node has 0 or 2 children
Perfect Tree: symmetric
Complete Tree: Fills from Left to Right
"""
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    ###### insert methods #########

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if value == temp.value:
                return False
            if value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def __r_insert(self, current_node, value):
        if current_node is None:
            return Node(value) # linked to node.left or node.right through return
        if value < current_node.value:
            current_node.left =self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node # returns the tree structure


    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    ###### contain methods #########

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
    
    def __r_contains(self, current_node, value):
        """ recursive """
        if current_node == None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    ###### delete methods #########

    def __delete_node(self, current_node, value):
        if current_node is None:
            return None
        if value < current_node.value:
            # 1
            current_node.left = self.__delete_node(current_node.left, value)
        if value > current_node.value:
            # 2
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            # returns to the 1 or 2 or root
            if current_node.left is None and current_node.right is None:
                # the node doesn't have leaves
                # None means that the current node will be set to None and removed
                return None
            elif current_node.left is None:
                # there is only right leaf
                # and it moves on the place of the current node
                current_node = current_node.right
            elif current_node.right is None:
                # there is only left leaf and current node = left leaf
                current_node = current_node.left
            else:
                pass
        return current_node
    
    def delete_node(self, value):
        self.root = __r_delete_node(self.root, value)

def printTree(node, level=0):
        # node = self.root
        if node != None:
            printTree(node.right, level + 1)
            if level == 0:
                print("* " + str(node.value))
            else:
                print(' ' * 4 * level + '-> ' + str(node.value))
            printTree(node.left, level + 1)

bst = BinarySearchTree()
bst.insert(43)
bst.insert(27)
bst.insert(56)
bst.insert(49)
bst.insert(19)
bst.insert(17)
bst.insert(29)
bst.r_insert(63)
bst.r_insert(28)



printTree(bst.root)

print(bst.r_contains(20))
print(bst.contains(17))
print(bst.r_contains(28))