a,b,c = input().split(",")
a = int(a)
b = int(b)
c = int(c)
if a>b:
    if a>c  :
     print("The largest Number is:",a)
    else:
        print("The largest number is:",c)
elif b>a:
    if b>c :
     print("The largest number is:",b)
    else:
        print("The largest number is:",c)
elif c>a:
    if c>b :
     print("The largest number is:",c)
    else:
        print("The largest number is:",b)
