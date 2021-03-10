from StackClass import Stack

def isOperator(char):
    if char=='+'or char=='-' or char=='*' or char=='/':
        return True
    else:
        return False
        
#postfix is AB+CD-*
    
def postfixxer(prefix):
    s=Stack()
    l=len(prefix)
    for i in range(l-1,-1,-1):
        if(isOperator(prefix[i])):
            temp=s.pop()
            temp2=temp+s.pop()+prefix[i]
            s.push(temp2)
        else:
            s.push(prefix[i])

    return s.peek()       
            
    

if __name__=="__main__":
    prefix='*+AB-CD'
    print('Prefix :',prefix)
    print('Postfix :',postfixxer(prefix))
