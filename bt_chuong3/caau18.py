# hinh vuong rong
'''
n=int(input("nhap n= "))
for i in range(n):
    if i==0 or i==(n-1):
        print('*'*n)
    else:
        print('*'+' '*(n-2)+'*')
'''
# hinh tam giac vuong 
'''
n = int(input("Nhập chiều cao n: "))
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)
'''
# hinh loop
n=int(input("nhap n (voi n la so le): "))
for i in range(n):
    """ """
    for j in range(n):
        if i==j or i==n//2 or (i<n//2 and j==0) or (i>n//2 and j==n-1):
            print('*',end='')  
        else:
            print(' ',end='')
    print()