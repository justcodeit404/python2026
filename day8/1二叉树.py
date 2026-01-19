# 2026-01-16  21:30:16
class Node():
    def __init__(self,elem=-1,lchild=None,rchild=None):
        self.elem = elem
        self.lchild = lchild
        self.rchild = rchild

class  BinaryTree():
    def __init__(self):
        self.root = None
        self.help_queue=[]

    def level_build_tree(self,node:Node):
        if self.root is None:
            self.root=node
            self.help_queue.append(node)
        else:
            self.help_queue.append(node)
            if self.help_queue[0].lchild is None:
                self.help_queue[0].lchild=node
            else:
                self.help_queue[0].rchild=node
                self.help_queue.pop(0)
    def preorder(self,current_node:Node):
        if current_node :
            print(current_node.elem,end=' ')
            self.preorder(current_node.lchild)
            self.preorder(current_node.rchild)

    def midorder(self,current_node:Node):
        if current_node :
            self.midorder(current_node.lchild)
            print(current_node.elem,end=' ')
            self.midorder(current_node.rchild)
    def postorder(self,current_node:Node):
        if current_node :
            self.postorder(current_node.lchild)

            self.postorder(current_node.rchild)
            print(current_node.elem, end=' ')
    def level_order(self):
        help_queue=[]
        help_queue.append(self.root)
        while help_queue:
            current_node = help_queue.pop(0)
            print(current_node.elem,end=' ')
            if current_node.lchild:
                help_queue.append(current_node.lchild)
            if current_node.rchild:
                help_queue.append(current_node.rchild)
if __name__=='__main__':
    tree=BinaryTree()
    for i in range(1,11):
        new_node=Node(i)
        tree.level_build_tree(new_node)
    tree.preorder(tree.root)
    print('')
    tree.midorder(tree.root)
    print('')
    tree.postorder(tree.root)
    print('')
    tree.level_order()
