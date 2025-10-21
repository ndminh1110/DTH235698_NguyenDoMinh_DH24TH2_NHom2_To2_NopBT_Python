year = int(input('Nhập vào một năm:'))
if(year%4==0 and year%100!=0)or(year%400==0):
    print('Năm ',year,' là năm nhuận.')
else:
    print('Năm ',year,' không phải là năm nhuận.')