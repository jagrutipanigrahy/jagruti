a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
choose=input("+,-,*,/")
if choose=="+":
    result=a+b
    print("the result is",result);
elif choose=="-":
    result=a-b
    print("the result is",result);
elif choose=="*":
    result=a+b 
    print("the result is",result);
elif choose=="/":
    result=a/b
    print("the result is",result)
else:
    ("invalid number")