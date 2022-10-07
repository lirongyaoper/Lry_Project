class BiTreeNode:
    def __init__(self,data):
        self.data=data
        self.lchild=None
        self.rchild=None
        self.parent=None

class BST_lry:
    def __init__(self,li=None):
        self.root = None
        if li:
            for val in li:
                self.root = self.insert(self.root,val)
    #递归插入
    def insert(self,node,val):
        if not node:
            node=BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild,val)
            node.lchild.parent=node
        elif val > node.data:
            node.rchild = self.insert(node.rchild,val)
            node.rchild.parent = node
        return node
    #非递归插入
    def insert_no_rec(self,val):
        p = self.root
        if not p:
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent=p
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return

     # 遍历：中序遍历
    def Centerorder_lry(self,ptr):
        if ptr != None:
            self.Centerorder_lry(ptr.lchild)
            print('[%2d]' %ptr.data,end='')
            self.Centerorder_lry(ptr.rchild)

    # 遍历：后序遍历
    def Postorder_lry(self,ptr):
        if ptr != None:
            self.Postorder_lry(ptr.lchild)
            self.Postorder_lry(ptr.rchild)
            print('[%2d]' %ptr.data,end='')

    # 遍历：前序遍历
    def Preorder_lry(self,ptr):
        if ptr != None:
            print('[%2d]' % ptr.data, end='')
            self.Preorder_lry(ptr.lchild)
            self.Preorder_lry(ptr.rchild)

    #查找_递归
    def query_lry(self,root,val):
        if root == None:
            return False
        if root.data == val:
            return True
        elif val < root.data:
            return  self.query_lry(root.lchild,val)
        elif val > root.data:
            return self.query_lry(root.rchild,val)
    #查找_递归
    def query_norec_lry(self,val):
        p=self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None

    #node是叶子结点
    def __remove_leaf_node(self,node):
        if not node.parent:
            self.root = None
        if node == node.parent.lchild:
            node.parent.lchild = None
        else:
            node.parent.rchild = None

    def __remove_haslchild_node(self,node):
        if not node.parent:
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_hasrchild_node(self,node):
        if not node.parent:
            self.root = node.rchild
            node.lchild.parent = None
        elif node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self, val):
        if self.root:
            node= self.query_norec_lry(val)
            if not node:
                return False
            if not node.lchild and not node.rchild:
                self.__remove_leaf_node(node)
            elif not node.rchild:
                self.__remove_haslchild_node(node)
            elif not node.lchild:
                self.__remove_hasrchild_node(node)
            else:
                min_node = node.rchild
                while min_node.lchild:
                    min_node = min_node.lchild
                node.data=min_node.data
                if min_node.rchild:
                    self.__remove_hasrchild_node(min_node)
                else:
                    self.__remove_leaf_node(min_node)





# root = None
# tree01 = BST_lry()
# li=[4,6,7,9,2,1,3,5,8]
# for var in li:
#     root = tree01.insert(root,var)
#
# tree01.Centerorder_lry(root)

tree = BST_lry([1,4,2,5,3,8,6,9,7])
tree.Centerorder_lry(tree.root)
print("")
tree.delete(9)
tree.Centerorder_lry(tree.root)


