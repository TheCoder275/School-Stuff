'''
num=int(input('Enter a number -->'))

for i in range(1,num+1):
    if num%i==0:
        print(i)
    else:
        continue
'

num=int(input("Enter a number -->"))
count=0
for i in range (1,num+1):
    if num%i==0:
        count=count+1
    else:
        continue
if count>2:
    print(num,"is not a prime number")
elif count<=2:
    print(num,"is a prime number")
    
