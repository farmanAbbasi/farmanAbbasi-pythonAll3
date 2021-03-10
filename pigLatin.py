def main():
    vowels=['a','e','i','o','u']
    finalStr=''
    words = list(input("Input Sentence:").split())

    for word in words:
        br=-1
        for i in range(len(word)):
            if word[i].lower() in vowels:
                br=i
                break
        if br == -1:
            finalStr+=word+'ay'+' '
        else:    
            finalStr+=str(word[br:])+str(word[:br])+'ay'+' '
                
    return finalStr.rstrip()       
    
print(main())
