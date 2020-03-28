a = 0
b = 1
fibList = [a,b]
n=int(input("Enter the number of terms in the sequence: "))
while(n-2) > 0:
    c=a+b
    a,b = b,c
    fibList.append(c)
    n=n-1
print(fibList)