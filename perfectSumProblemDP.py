
#memoiztion....
def perfectSum(arr,total):
    mem={}
    return counter(arr,total,len(arr)-1,mem)

def counter(arr,total,i,mem):
    key=str(total)+':'+str(i)
    if key in mem:
        return mem[key]
    elif total==0:
        return 1
    elif total<0:
        return 0
    elif i<0:
        return 0
    elif total<arr[i]:
        to_return=counter(arr,total,i-1,mem)
    else:
        to_return =(counter(arr,total-arr[i],i-1,mem)+counter(arr,total,i-1,mem))
    mem[key]=to_return
    return to_return
    

    



if __name__=='__main__':
    k=16
    arr=[2,4,6,10]
    print(perfectSum(arr,k))





