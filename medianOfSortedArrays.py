
def medianFinder(arr1,arr2):
    if len(arr1)>len(arr2):
        medianFinder(arr2,arr1)
        
    x=len(arr1)
    y=len(arr2)
    low=0
    high=x

    while(low<=high):
        partitionX=int((low+high)/2)
        partitionY=int((x+y+1)/2)-partitionX

        maxLeftX= -99999999 if partitionX==0 else arr1[partitionX-1]
        minRightX=-99999999 if partitionX==x else arr1[partitionX]

        maxLeftY=-99999999 if partitionY==0 else arr2[partitionY-1]
        minRightY=-99999999 if partitionY==y else arr2[partitionY]

        if(maxLeftX<=minRightY and maxLeftY<=minRightX):
            if (x+y)%2!=0:
                return max(maxLeftX,maxLeftY)
            else:
                
                return (max(maxLeftX,maxLeftY)+min(minRightX,minRightY))/2
        elif maxLeftX>minRightY:
            high=partitionX-1#decrement in high
        else:
            low=partitionX+1#increment in low

        
        
    

if __name__=='__main__':
    arr1=[4,6,7,12,15,34,40,50]
    arr2=[10,12,12,13,14,15]
    print(sorted(arr1+arr2))
    print(medianFinder(arr1,arr2))
