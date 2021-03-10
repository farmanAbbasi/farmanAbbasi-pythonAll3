
a=[1,3,2,0]

#4 wants to be where 3 is ->3 ->2->1->4, since cycle so n-1 swaps
#so 4-1 swaps


def minSwapper(a):
    counter=0
    length=len(a)
    arr_dict={}
    for i, item in enumerate(a):
        arr_dict[item]=i
    print(arr_dict)
    checked=[False]*length
    for key, value in sorted(arr_dict.items(), key = lambda x: x[0]):
        
        print(key,' ',value)
        if checked[key] or key == value:
            continue
        c_count=0
        value=key
        while not checked[value]:
            checked[value]=True
            value=arr_dict[value]
            c_count+=1
        counter+=c_count-1
    return counter    
            
        
        
        

x=minSwapper(a)
print(x)

    
