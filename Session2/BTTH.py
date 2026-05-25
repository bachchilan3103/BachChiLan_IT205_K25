import datetime

name = input("Nhập tên bệnh nhân: ").strip()
year_of_birth = int(input("Nhập năm sinh: "))
days_sick = int(input("Nhập số ngày bị bệnh: "))
temperature = float(input("Nhập nhiệt độ cơ thể (°C): "))
exam_fee = float(input("Nhập chi phí khám: "))

current_year = datetime.datetime.now().year

if not name:
    print("Lỗi: Tên không được để trống.")
    exit()
if year_of_birth < 1900 or year_of_birth > current_year:
    print("Lỗi: Năm sinh không hợp lệ.")
    exit()
if days_sick < 0:
    print("Lỗi: Số ngày bị bệnh phải ≥ 0.")
    exit()
if temperature < 30 or temperature > 45:
    print("Lỗi: Nhiệt độ không hợp lệ.")
    exit()
if exam_fee <= 0:
    print("Lỗi: Chi phí khám phải > 0.")
    exit()

age = current_year - year_of_birth
extra_fee = exam_fee * 0.1
total_fee = exam_fee + extra_fee

if temperature > 38 and days_sick > 3:
    health_status = "Nguy hiểm"
elif temperature > 38:
    health_status = "Sốt cao"
elif temperature > 37.5:
    health_status = "Sốt nhẹ"
else:
    health_status = "Bình thường"

if health_status == "Nguy hiểm":
    if age > 60:
        priority = "Cấp cứu"
    else:
        priority = "Ưu tiên cao"
else:
    priority = "Bình thường"

cost_level = "Cao" if total_fee > 500000 else "Thấp"

print("\n===== KẾT QUẢ ĐÁNH GIÁ =====")
print(f" Tên bệnh nhân: {name}")
print(f" Tuổi: {age}")
print(f" Nhiệt độ: {temperature}°C")
print(f" Tình trạng sức khỏe: {health_status}")
print(f" Mức độ ưu tiên: {priority}")
print(f" Chi phí khám: {exam_fee:,.0f} VND")
print(f" Phụ phí (10%): {extra_fee:,.0f} VND")
print(f" Tổng chi phí: {total_fee:,.0f} VND")
print(f" Mức chi phí: {cost_level}")
