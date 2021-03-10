from difflib import *
str1='abcdefgfgfgfg'#Search in this 
str2='zbdfg'#for this
start=0
maxStr=''
maxStrLen=0

#note subsequence returns Match(a,b,size)i.e [a:a+size]or [b:b+size]
#matching for longest substring possible

for i in range(len(str1)-len(str2)+1):
    subStr1=str1[i:i+len(str2)]
    
    s = SequenceMatcher(None,subStr1,str2)#in substring finding for test string str2
    ss=s.find_longest_match(0,len(subStr1),0,len(str2))
    substringMatched=subStr1[ss.a:ss.a+ss.size]
    if(maxStrLen<len(substringMatched)):
        maxStr=substringMatched
        maxStrLen=len(substringMatched)

        
print(maxStr)
print(maxStrLen)
    


