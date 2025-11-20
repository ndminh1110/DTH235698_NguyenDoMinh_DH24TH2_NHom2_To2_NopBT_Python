from math import sqrt

a=float(input("Nhap canh a: "))
b=float(input("Nhap canh b: "))
c=float(input("Nhap canh c: "))

#kiem tra tam giac
if a+b<c or a+c<b or b+c<a:
    print("Khong phai tam giac")
else:
    print("La tam giac")

def chuvi(a,b,c):
    return a+b+c

def dientich(a,b,c):
    p=(a+b+c)/2
    return sqrt(p*(p-a)*(p-b)*(p-c))

print("Chu vi tam giac: ", chuvi(a,b,c))
print("Dien tich tam giac: ", dientich(a,b,c))