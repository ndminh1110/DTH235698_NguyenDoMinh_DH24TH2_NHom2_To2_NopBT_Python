day=int(input("Nhap 1 ngay: "))
month=int(input("Nhap vao 1 thang: "))
year=int(input("Nhap vao 1 nam: "))
if month in (1,2,3,4,5,6,7,8,9,10,11,12):
    if month in (1,3,5,7,8,10):
        if day==31:
            day=1
            month+=1
        else:
            day+=1
    elif month in (4,6,9,11):
        if day==30:
            day=1
            month+=1
        else:
            day+=1
    elif month==2:
        if day<28:
                day+=1
        if(year%4==0 and year%100!=0)or(year%400==0):
            if day ==29:
                day=1
                month+=1
        elif day==28:
                day=1
                month+=1
    elif month==12:
        if day==31:
            day=1
            month=1
            year+=1
        else:
            day+=1
print(day,"/",month,"/",year)