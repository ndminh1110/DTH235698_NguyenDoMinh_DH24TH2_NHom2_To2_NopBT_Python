while True:
 try:
  month=int(input("Nhập tháng: "))
  if month in(1,3,5,7,8,10,12):
    print("Tháng ", month," có 31 ngày.")
    break
  elif month in(4,6,9,11):
    print("Tháng ", month," có 30 ngày.")
    break
  elif month ==2:
    year=int(input("Nhập năm: "))
    if(year%4==0 and year%100!=0)or(year%400==0):
        print("Tháng ", month," có 29 ngày.")
        break
    else:
        print("Tháng ", month," có 28 ngày.")
        break
 except ValueError:
    print("Tháng không hợp lệ. Vui lòng nhập lại.")