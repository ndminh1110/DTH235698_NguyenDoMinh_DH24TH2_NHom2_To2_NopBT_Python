n=int(input("Nhập 1 số có 2 chữ số: "))
if n<=0 and n>100:
    print("Số không hợp lệ. ")
else:
    chuc=n//10
    donvi=n%10

    so=["không","một","hai","ba","bốn","năm","sáu","bảy","tám","chín"]
    if n<10:
        print(so[n].capitalize())
    elif chuc==1:
        if donvi==0:
            print("Mười")
        elif donvi==5:
            print("Mười lăm")
        else:
            print("Mười "+ so[donvi])
    else:
        doc = so[chuc] + " mươi"
        if donvi == 0:
            print(doc.capitalize())
        elif donvi == 1:
            print((doc + " mốt").capitalize())
        elif donvi == 5:
            print((doc + " lăm").capitalize())
        else:
            print((doc+ " " + so[donvi]).capitalize())

