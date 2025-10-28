def GiaiThua(a):
    if a==0:
        return 1
    else:
        return a*GiaiThua(a-1)
def TinhBieuThuc(a,b):
    tong=0
    for n in range(0,b+1):
        m=2*n+1
        tu=a**m
        mau=GiaiThua(m)
        kq=tu/mau
        tong+=kq
    return tong
x=int(input("Nhập x: "))
n=int(input("Nhap n: "))
print("kq= ", TinhBieuThuc(x,n))