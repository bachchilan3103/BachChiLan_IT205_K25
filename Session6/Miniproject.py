laptop = 0
phone = 0
tablet = 0

print(" == CHƯƠNG TRÌNH QUẢN LÍ KHO == ")

while True:
    print("1. Xem tồn kho")
    print("2. Nhập hàng")
    print("3. Xuất hàng")
    print("4. Báo hàng tồn kho kh đủ")
    print("5. Thoát")

    option = input("Nhập lựa chọn 1-5: ")

    if option == "1":
        print("-- BÁO CÁO TỒN KHO --")
        print("Laptop:", laptop, "cái")
        print("Điện thoại:", phone, "cái")
        print("Máy tính bảng:", tablet, "cái")

        print("\nBiểu đồ tồn kho:")
        print("Laptop:", "*" * laptop)
        print("Điện thoại:", "*" * phone)
        print("Máy tính bảng:", "*" * tablet)

    elif option == "2":
        print("\n -- NHẬP HÀNG --")
        print("1. Laptop\n 2. Điện thoại\n 3. Máy tính bảng")
        item = input("Chọn mặt hàng để nhập: ")

        if item == "1":
            item_name = "Laptop"
        elif item == "2":
            item_name = "Điện thoại"
        elif item == "3":
            item_name = "Máy tính bảng"
        else:
            print("Lựa chọn không đúng.")
            continue

        amount = int(input("Nhập số lượng cần nhập: "))
        while amount < 0:
            print("Số lượng không được âm vui lòng nhập lại.")
            amount = int(input("Nhập số lượng cần nhập: "))

        if item == "1":
            laptop = laptop + amount
        elif item == "2":
            phone = phone + amount
        else:
            tablet = tablet + amount

        print("Đã nhập được", amount, item_name, "cái")

    elif option == "3":
        print("\n -- XUẤT HÀNG -- ")
        print("1. Laptop\n 2. Điện thoại\n 3. Máy tính bảng")
        item = input("Chọn mặt hàng để xuất: ")

        if item == "1":
            item_name = "Laptop"
            current_stock = laptop
        elif item == "2":
            item_name = "Điện thoại"
            current_stock = phone
        elif item == "3":
            item_name = "Máy tính bảng"
            current_stock = tablet
        else:
            print("Lựa chọn không đúng.")
            continue

        amount = int(input("Nhập số lượng cần xuất: "))
        while amount < 0:
            print("Số lượng không được âm vui lòng nhập lại.")
            amount = int(input("Nhập số lượng cần xuất: "))

        if amount > current_stock:
            print("Không đủ hàng để xuất kho\n")
            continue

        if item == "1":
            laptop = laptop - amount
        elif item == "2":
            phone = phone - amount
        else:
            tablet = tablet - amount

        print("Đã xuất kho", amount, item_name)

    elif option == "4":
        print("\n -- CẢNH BÁO TỒN KHO THẤP -- ")
        if laptop < 10:
            print("Laptop sắp hết hàng còn", laptop, "cái")
        if phone < 10:
            print("Điện thoại sắp hết hàng còn", phone, "cái")
        if tablet < 10:
            print("Máy tính bảng sắp hết còn", tablet, "cái")

    elif option == "5":
        print("Thoát")
        break
    else:
        print("Lựa chọn không đúng bạn hãy nhập lại.")