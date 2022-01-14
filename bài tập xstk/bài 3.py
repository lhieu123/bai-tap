def soThuanNghich(n):
    i_1 = str(n)    
    i_2 = i_1[::-1] 
    if (i_1 == i_2):
        print(n, "là số thuận nghịch!")
    else:
        print(n, "không phải là số thuận nghịch!")
 
ten = input("Nhập họ và tên: ")
print("Họ và tên đầy đủ là:", ten)
n = int(input("Nhập số nguyên dương n: "))
soThuanNghich(n)