def add(a, b):
    print(a, " + ", b, " = ", a+b)

def sub(a, b):
    print(a, " - ", b, " = ", a-b)

def mu(a, b):
    print(a, " * ", b, " = ", a*b)

def div(a, b):
    print(a, " / ", b, " = ", a/b)

print("Chọn chức năng bạn muốn thực hiện: ")
print("1. Cộng ")
print("2. Trừ ")
print("3. Nhân ")
print("4. Chia ")
print("5. Thoát ")

while True:
    try:
        user = int(input("Chọn chức năng bạn muốn thực hiện: "))
    except ValueError:
        print("Vui lòng nhập số")
        continue
    
    if user <1 or user >5 :
        print("Chức năng không tồn tại, vui lòng chọn lại")
        continue
    
    if user == 1:
        a = int(input("Nhập số thứ nhất: "))
        b = int(input("\n Nhập số thứ hai: "))
        add(a, b)
    elif user == 2:
        a = int(input("Nhập số thứ nhất: "))
        b = int(input("\n Nhập số thứ hai: "))
        sub(a, b)
    elif user ==3:
        a = int(input("Nhập số thứ nhất: "))
        b = int(input("\n Nhập số thứ hai: "))
        mu(a, b)
    elif user ==4:
        a = int(input("Nhập số thứ nhất: "))
        b = int(input("\n Nhập số thứ hai: "))
        div(a, b)
    elif user ==5:
        print("Tạm biệt bạn ơi!")
        quit()
