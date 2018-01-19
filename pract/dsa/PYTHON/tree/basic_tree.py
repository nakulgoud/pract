'''
TODO: implement strategy pattern
eg: print: 
1. Inorder
2. Preorder
3. Post order
4. Level order
5. circumference nodes only
6. Vertical
7. print all root to leaf path
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

    def find_max_height(self):
        if self.root is None:
            return 0
        return self._find_max_height(self.root)

    def _find_max_height(self, cur_node):
        if cur_node is None:
            return 0
        return 1 + max(self._find_max_height(cur_node.left), self._find_max_height(cur_node.right))

    def find_max_width(self):
        pass

    def find_level_of_node(self, data):
        '''
        Find at which level the node is present in the tree
        '''
        pass

    def size(self):
        '''
        count the number of nodes in the tree
        '''
        if self.root is None:
            return 0
        else:
            return self._size(self.root)

    def _size(self, cur_node):
        if cur_node is None:
            return 0
        return self._size(cur_node.left) + 1 + self._size(cur_node.right)

    def has_path_sum(self, sum):
        '''
        return true if the tree has a root-to-leaf path such that adding up
        all the values along the path equals the given sum
        '''
        pass

    def mirror(self):
        pass
    
    def same_tree(self, other_tree):
        '''
        Given two binary trees, return true if they are structurally identical
        -- they are made of nodes with the same values arranged in the same
        way.
        '''
        pass
    
    def is_bst(self):
        if self.root is None:
            return True
        return self._is_bst(self.root, self.root.data, self.root.data)
    
    def _is_bst(self, cur_node, min_val, max_val):
        if cur_node is None:
            return True
        if cur_node.left and cur_node.left.data > min_val:
            print 'Hey cur_node:{} left:{} left.data:{} min_val:{}'.format(cur_node.data, cur_node.left, cur_node.left.data, min_val)
            return False
        if cur_node.right and cur_node.right.data <= max_val:
            print 'Hey right:{} right.data:{} max_val:{}'.format(cur_node.right, cur_node.right.data, max_val)
            return False
        return self._is_bst(cur_node.left, min_val, cur_node.data) and self._is_bst(cur_node.right, cur_node.data, max_val)

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
        if self.root is None:
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

    def search(self, data):
        if self.root is None:
            return False
        cur_node = self.root
        while(cur_node):
            if cur_node.data == data:
                return True
            elif data < cur_node.data:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right

        return False

    def find_min_value(self):
        if self.root is None:
            return None
        return self._find_min_value(self.root)

    def _find_min_value(self, cur_node):
        while(cur_node.left is not None):
            cur_node = cur_node.left
        return cur_node.data

    def find_max_value(self):
        if self.root is None:
            return None
        return self._find_max_value(self.root)

    def _find_max_value(self, cur_node):
        while(cur_node.right is not None):
            cur_node = cur_node.right
        return cur_node.data

    def delete_node(self, data):
        pass

if __name__ ==  "__main__":
    bst = BinarySearchTree()
    data_list = [1,6,3,4,5]
    for data in data_list:
        bst.insert_node(data)

    bst.print_tree()
    element_to_find = 4
    is_found = bst.search(element_to_find)
    print '{} is there?: {}'.format(element_to_find, is_found)
    #bst.delete_node(1)
    #bst.print_tree()
    print '\nMax value is:{}'.format(bst.find_max_value())
    print '\nMin value is:{}'.format(bst.find_min_value())
    print '\nsize of tree is:{}'.format(bst.size())
    print '\nis bst:{}'.format(bst.is_bst())

