from StackClass import Stack

def isOperator(char):
    if char=='+'or char=='-' or char=='*' or char=='/':
        return True
    else:
        return False
        
#postfix is AB+CD-*
def prefixxer(postfix):
    s=Stack()
    l=len(postfix)
    for i in range(l):
        if(isOperator(postfix[i])):
            temp=''
            temp2=''
            temp=s.pop()
            temp2=postfix[i]+s.pop()+temp
            s.push(temp2)
        else:
            s.push(postfix[i])

    return s.peek()       
            
    

if __name__=="__main__":
    postfix='ABC/-AK/L-*'
    print('Postfix :',postfix)
    print('Prefix :',prefixxer(postfix))
