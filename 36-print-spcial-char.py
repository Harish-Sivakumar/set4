n=input()
count=0
for i in n:
    if(i.isalnum()!=True):
        count=count+1
print(count)