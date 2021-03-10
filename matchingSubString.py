str1='aabccccdbca'
str2='ccc'
start=0
#creating a substring of length  of str2 from str1 
for i in range(len(str1)-len(str2)+1):
    subStr1=str1[i:i+len(str2)]
    if(str2==subStr1):
        print('found at {0}'.format(i+1))
    
        
    
    
