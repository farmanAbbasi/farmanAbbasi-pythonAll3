def solution():
    def isSafe(row,col):
        #for checking in straight line
        for i in range(N):
            if arr[row][i]==1:
                return False
        #for checking in hori line        
        for i in range(N):
            if arr[i][col]==1:
                return False        
        
        #top diagonal left
        r=row
        c=col
        while r!=0 and c!=0:
            r=r-1
            c=c-1
            if arr[r][c]==1:
                return False
        
        r3=row
        c3=col
        #bottom diagonal right
        while r3!=N-1 and c3!=N-1:
            r3=r3+1
            c3=c3+1
            if arr[r3][c3]==1:
                return False
        #top right diagonal
        for i, j in zip(range(row, -1, -1),  
                        range(col, N, 1)): 
            if arr[i][j] == 1: 
                return False
        
        
        # Check lower diagonal on left side 
        for i, j in zip(range(row, N, 1),  
                    range(col, -1, -1)): 
            if arr[i][j] == 1: 
                return False  
       
        return True        
    
    def queen(row):
        print("rooooo",row)
        if row==len(arr):
            return True
        for i in range(len(arr)):
            print("row, ",row,"i ",i)
            if isSafe(row,i):
                
                arr[row][i]=1 
                print(i," : ",arr)
                print(row+1)
                ans=queen(row+1)
                if ans==True:
                    return True
                else:
                    arr[row][i]=0
        return False            
            
    
    
    
    N=5
    arr=[[0 for i in range(N)] for j in range(N)]
    print(arr)
    ans=queen(0)
    print(arr)
    print("ans",ans)
solution()    


