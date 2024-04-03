a=int(input())
b=int(input())
c=input()
d=True
while c !="":
    if int(c) not in range(a,b+1):
        d = False
    c=input()
print(d)