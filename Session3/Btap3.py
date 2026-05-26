# range(1,4) se chay dung 3l cho 3 nvien
# ktra dkien hop le thi in phieu ho so kh thi se canh bao loi va bo qua nvien

for employee_number in range(1, 4):
    print(f" --- Nhap thong tin cho nvien co so la {employee_number} --- ")
    employee_code = input("Nhap ma nvien: ")
    employee_name = input("Nhap ten nvien: ")
    department = input("Nhap phong ban: ")

    if employee_code == "" or employee_name == "":
        print("Du lieu hoac ten khong dung.")
    else:
        print(" --- Phieu ho so dien tu --- ")
        print(f"Ma nvien: {employee_code}")
        print(f"Ho va ten: {employee_name}")
        print(f"Phong ban: {department}")
        print("Ho so nvien dc tao thanh cong")
print("Qtrinh khoi tao ho so nvien da hoan tat.")
