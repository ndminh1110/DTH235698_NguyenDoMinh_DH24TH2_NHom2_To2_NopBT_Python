from math import sqrt

a=float(input("Nhập số a: "))
b=float(input("Nhập số b: "))
c=float(input("Nhập số c: "))
if a==0:
    if b==0 and c==0:
        print("Phương trình vô số nghiệm.")
    elif b==0 and c!=0:
        print("Phương trình vô nghiệm.")
    else:
        x=-b/a
        print("Phương trình có một nghiệm: x= ",x)
else:
    delta=b**2-4*a*c
    if delta<0:
        print("Phương trình vô nghiệm.")
    elif delta==0:
        x=-b/(2*a)
        print("Phương trình có nghiệm kép: x1= x2= ",x)
    else:
        x1=(-b+sqrt(delta))/(2*a)
        x2=(-b-sqrt(delta))/(2*a)
        print("Phương trình có hai nghiệm phân biệt:")
        print("x1= ",x1)
        print("x2= ",x2)