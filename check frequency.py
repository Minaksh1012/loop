string=input("enter the string")
c=input("enter character to check frequency")
count=0
for i in string:
    if i==c :
        count+=1
print(c,"occurs",count,"times")        