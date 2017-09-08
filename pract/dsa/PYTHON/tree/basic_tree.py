'''
TODO: implement strategy pattern
'''
class BinaryTreeNode():
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

class BinaryTree(object):
    def __init__(self):
        self.root = None
    
    def print_tree(self):
        if self.root:
            self._print_tree(self.root)

    def _print_tree(self, cur_node):
        if not cur_node:
            return

        self._print_tree(cur_node.left)
        print cur_node.data
        self._print_tree(cur_node.right)

    def is_binary_search_tree(self):
        '''
        Checks if given tree is binary search tree or not
        '''
        pass

class BinarySearchTree(BinaryTree):
    '''
               |Operation|        Complexity
               |         |  Average    |   Worst
    ====================================================
    1.         |  Insert |  O(log2 n)  |  O(n)
    ----------------------------------------------------
    2.         |  Search |  O(log2 n)  |  O(n)
    ----------------------------------------------------
    3.         |  Delete |  O(log2 n)  |  O(n) 
    ----------------------------------------------------
    4.         |  Space  |  O(n)       |  O(n) 
    ----------------------------------------------------

    Note: This tree can become skewed, which may cause search time to be O(n)
    '''
    def __init__(self):
        super(BinarySearchTree, self).__init__()

    def insert_node(self, data):
        if self.root == None:
            self.root = BinaryTreeNode(data)
        else:
            self._insert_node(data, self.root)

    def _insert_node(self, data, cur_node):
        if data < cur_node.data:
            if cur_node.has_left_child():
                self._insert_node(data, cur_node.left)
            else:
                cur_node.left = BinaryTreeNode(data)
        else:
            if cur_node.has_right_child():
                self._insert_node(data, cur_node.right)
            else:
                cur_node.right = BinaryTreeNode(data)

if __name__ ==  "__main__":
    bst = BinarySearchTree()
    data_list = [1,6,3,4,5]
    for data in data_list:
        bst.insert_node(data)

    bst.print_tree()
