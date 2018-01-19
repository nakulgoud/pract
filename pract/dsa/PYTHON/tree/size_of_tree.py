class Node():
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

class Tree():
    def __init__(self):
        self._root = None

    def add_element(self, value):
        if self._root is None:
            self._root = Node(value)
        else: 
            self._insert_node(value, self._root)

    def _insert_node(self, value, cur_root):
        if value < cur_root._value:
            if cur_root._left:
                self._insert_node(value, cur_root._left)
            else:
                cur_root._left = Node(value) 
        else:
            if cur_root._right:
                self._insert_node(value, cur_root._right)
            else:
                cur_root._right = Node(value)


    def print_tree(self):
        self._print_tree(self._root)

    def _print_tree(self, root):
        if root is None:
            return

        self._print_tree(root._left)
        self._print_tree(root._right)
        print root._value

    def print_tree_levelwise(self):
        if self._root is None:
            return

        this_level = [self._root]
        while this_level:
            next_level = []
            for element in this_level:
                print element._value,
                if element._left:
                    next_level.append(element._left)
                if element._right:
                    next_level.append(element._right)
            print
            this_level = next_level

    def print_non_recursive_inorder(self):
        cur_node = self._root
        s = []
        while(True):
            if cur_node:
                s.append(cur_node)
                cur_node = cur_node._left

            else:
                if s:
                    cur_node = s.pop()
                    print cur_node._value
                    cur_node = cur_node._right
                else:
                    break
    def print_non_recursive_preorder(self):
        s = [self._root]
        while s:
            element = s.pop()
            print element._value,
            if element._right:
                s.append(element._right)
            if element._left:
                s.append(element._left)



    def print_non_recursive_postorder(self):
        s1 = [self._root]
        s2 = []

        while(s1):
            element = s1.pop()
            s2.append(element)
            if element._left:
                s1.append(element._left)
            if element._right:
                s1.append(element._right)

        while(s2):
            element = s2.pop()
            print element._value

    def height(self):
        if self._root is None:
            return 0
        return self._height(self._root)

    def _height(self, cur_node):
        if cur_node is None:
            return 0

        return 1 + max(self._height(cur_node._left), self._height(cur_node._right))

    def diameter(self):
        return self._diameter(self._root)

    def _diameter(self, cur_node):
        if cur_node is None:
            return 0

        lheight = self._height(cur_node._left)
        rheight = self._height(cur_node._right)
        ldiameter = self._diameter(cur_node._left)
        rdiameter = self._diameter(cur_node._right)
        return max((lheight + rheight + 1), max(ldiameter, rdiameter))

tree_instance = Tree()
tree_instance.add_element(5)
tree_instance.add_element(4)
tree_instance.add_element(6)
tree_instance.add_element(7)
#tree_instance.print_tree()
tree_instance.print_tree_levelwise()
#tree_instance.print_non_recursive_inorder()
#tree_instance.print_non_recursive_preorder()
#tree_instance.print_non_recursive_postorder()
#print tree_instance.height()
#print tree_instance.diameter()
print tree_instance.
'''
1. is BST
2. delete_node
3. mirror
4. diameter ()
5. check_2_trees_same
6. Construct B_tree from inorder and pre_order
7. width of a tree
9. lowest common ancestor
10. height balanced tree
'''
