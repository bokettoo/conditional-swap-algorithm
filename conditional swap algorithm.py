a = int(input("enter number a :"))
b = int(input("enter number b :"))

if a*b>0: 
    z=a
    a=b
    b=z
    print(f"a: {a} and b: {b} ")
else: 
    x=a+b
    y=a*b
    a=x
    y=b

    print(f" a: {a} and b: {b}")