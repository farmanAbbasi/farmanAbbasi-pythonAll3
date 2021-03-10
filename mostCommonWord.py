from collections import Counter

s="Lorem Ipsum Lorem Ipsum is simply dummy text of the printing and type setting industry"
         
banned=['LORem']
banned2=[x.lower() for x in banned]
print(banned2)
maxi=-999
maxword=''
ll={}
ss=s.lower().split(' ')
#print(ss)
ll=Counter(ss)
print(ll)


for word in ll:
    if word not in banned2:
        temp=ll[word]
        if maxi<temp:
            maxword=word
            maxi=temp
print(maxword)
print(maxi)
