while True:
    print(" === QUAN LI CHAM CONG CHO NHAN VIEN === ")
    num_employees = int(input("Nhap so luong nvien: "))

    for i in range(1, num_employees + 1):
        print(f" Nhan vien {i}")
        name = input("Ten nvien: ")
        days_worked = int(input("So ngay nvien di lam: "))

        print(" Thong tin nhan vien: ")
        print(f"Ten: {name}")
        print(f"So ngay nvien di lam: {days_worked}")

        if days_worked < 20:
            print("Can chuyen can hon")
        else:
            print("Nvien chuyen can rat tot")

    choice = input("Tiep tuc chuong trinh y/n : ").lower()
    if choice == "n":
        print("Ctrinh ket thuc")
        break
