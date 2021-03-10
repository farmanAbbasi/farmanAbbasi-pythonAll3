def preorder(root):
    '''
    :param root: root of the given tree.
    :return: a list containing pre order Traversal of the given tree.
    {
        class Node:
        def _init_(self,val):
            self.data = val
            self.left = None
            self.right = None
    }
    '''
    # code here
    
    if root is  None:
        return []
    
    ans=[]    
    s=deque()
    s.append(root)

    while(len(s)>0):
        temp=s.pop()
        ans.append(temp.data)
        if temp.right:
            s.append(temp.right)
        if temp.left:
            s.append(temp.left)
    return ans   

    