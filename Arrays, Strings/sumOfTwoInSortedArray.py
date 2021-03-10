def twoSum(self, numbers, target):
        #using two pointer method as it is sorted array
        i=0
        j=len(numbers)-1
        while i<j:
            if numbers[i]+numbers[j]>target:
                j=j-1
            elif numbers[i]+numbers[j]<target:
                i=i+1
            else:
                return [i+1,j+1]
        return -1    
            
