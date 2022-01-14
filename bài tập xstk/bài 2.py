def find_sum(n):
    tongbien = 0
    stt = n
    while (n > 0):
        tongbien = tongbien + n % 10
        n = int(n / 10)
    print("Tổng các chữ số của", stt, "là:", tongbien)
 
middleName = input("Nhập tên đệm: ")
print("Tên đệm vừa nhập:", middleName)
 
n = int(input("Nhập số nguyên dương n = "))
find_sum(n)