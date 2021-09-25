x = [1, 1, 2, 6, 8, 9, 4, 5, 6, 45, 34, 66, 44, 37, 78]
print("x: ", x)
print("list2: ")
for i in range(0, 15):
    if(x[i] < 30):
        y = x[i]
        print(list2, end=", ")
print("Nhập a: ")
a = input("")
print("Những số nhỏ hơn a là: ")
for i in range(0, 15):
    if(x[i] < int(a)):
        z = x[i]
        print(z, end=", ")