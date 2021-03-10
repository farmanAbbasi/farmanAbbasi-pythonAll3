from StackClass import Stack

def isOperator(char):
    if char=='+'or char=='-' or char=='*' or char=='/':
        return True
    else:
        return False
        
#postfix is AB+CD-*
    
def infixxer(postfix):
    s=Stack()
    l=len(postfix)
    for i in range(l):
        if(isOperator(postfix[i])):
            temp=s.pop()
            temp2='('+s.pop()+postfix[i]+temp+')'
            s.push(temp2)
        else:
            s.push(postfix[i])

    return s.peek()       
            
    

if __name__=="__main__":
    postfix='ab*c+'
    print('Postfix :',postfix)
    print('Infix :',infixxer(postfix))
