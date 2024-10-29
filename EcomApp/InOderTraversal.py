
class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inOrder(ls):
    try:
        if ls == None :
            #print('Empty')
            return []
       
        if ls.left == None and ls.right ==None:
            print(f"{ls.value}")
            return []
            
        if ls:
            inOrder(ls.left)
            print(f"{ls.value}")
            inOrder(ls.right)
            return ls.left   
    except:
        print('exception occured')        


node3= Node('third',None, None)
node2= Node('second',None, None)
node1= Node('first',node2, node3)

#print(node2.left,node1.value)

inOrder(node1)    
