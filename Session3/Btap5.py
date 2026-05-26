# truong du lieu bao gom: ma nvien(employee_id), ho ten(employee_name), luong htai(current_salary), luong moi(updated_salary), diem KPI(performance_score)

print("Tap thuc nghiem Kiosk")
while True:
    employee_id = input("Nhap ma nvien: ")
    employee_name = input("Nhap ho va ten: ")
    current_salary = float(input("Nhap luong hien tai (VND): "))
    updated_salary = float(input("Nhap luong moi (VND): "))
    performance_score = int(input("Nhap diem KPI: "))

    if current_salary <= 0 or updated_salary <= 0 or performance_score < 0 or performance_score > 10:
        print("Du lieu kh hop le.")
    else:
        print("Du lieu hop le.")
    break

print(" --- HO SO NHAN SU DIEN TU --- ")
print(f"Ma nvien: {employee_id}")
print(f"Ho va ten: {employee_name}")
print(f"Luong htai: {current_salary:,.0f} VND")
print(f"Luong moi: {updated_salary:,.0f} VND")
print(f"Diem KPI: {performance_score}/10")

print(" --- LOG HE THONG --- ")
print(f"employee_id: {type(employee_id)}")
print(f"employee_name: {type(employee_name)}")
print(f"current_salary: {type(current_salary)}")
print(f"updated_salary: {type(updated_salary)}")
print(f"performance_score: {type(performance_score)}")

print("Dang thoat chuong trinh!")
