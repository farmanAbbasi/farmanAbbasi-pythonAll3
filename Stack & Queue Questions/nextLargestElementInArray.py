# class Stack:
#      def __init__(self):
#          self.items = []

#      def isEmpty(self):
#          return self.items == []

#      def push(self, item):
#          self.items.append(item)

#      def pop(self):
#          return self.items.pop()

#      def peek(self):
#          return self.items[len(self.items)-1]

#      def size(self):
#          return len(self.items)
         
         
def nextLargestNumber(arr):
    if arr==None or len(arr)==0:
        return [-1]
    s=[]
    a=[-1]*len(arr)
    for i in range(len(arr)):
        if(len(s)==0):
            s.append(i)
        j=i
        while(len(s)>0  and j<len(arr)-1):
            j=j+1
            if arr[s[len(s)-1]] >arr[j]:
                s.append(i)
            else:
                a[s.pop()]=arr[j]
                j-=1
    return a        
    
if __name__ =='__main__': 
    print(nextLargestNumber([3,1]))    
    
    
    
    
    
    
    
    
    
    
    
    
         
         
