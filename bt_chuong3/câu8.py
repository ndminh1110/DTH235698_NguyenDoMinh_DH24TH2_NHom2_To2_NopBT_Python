soA=int(input("Nhập số A: ")   )
soB=int(input("Nhập số B: ")   )
toanTu=input("Nhập phép toán: ")
if(toanTu=="+"):
    kq=soA+soB
    print("Kết quả: ",kq)
elif(toanTu=="-"):
    kq=soA-soB
    print("Kết quả: ",kq)
elif(toanTu=="*"):
    kq=soA*soB
    print("Kết quả: ",kq)
else:
    kq=soA/soB
    print("Kết quả: ",kq)