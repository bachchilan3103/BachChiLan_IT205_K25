# patient_name: ho ten str
# patient_code: ma benh nhan str
# body_temperature: nhiet do co the float
# heart_rate: nhip tim int
# weight: can nag float

print(" === PHÒNG TIẾP NHẬN VÀ KHAI BÁO Y TẾ === ")
patient_name = input("Nhập họ và tên bệnh nhân: ")
patient_code = input("Nhập mã bệnh nhân: ")
body_temperature = float(input("Nhập nhiệt độ cơ thể: "))
heart_rate = int(input("Nhập nhịp tim: "))
weight = float(input("Nhập cân nặng: "))

print(" --- PHIẾU KHÁM BỆNH ĐIỆN TỬ --- ")
print("Họ tên bệnh nhân:", patient_name)
print("Mã bệnh nhân:", patient_code)
print("Nhiệt độ cơ thể:", body_temperature, "C")
print("Nhịp tim:", heart_rate, "nhịp")
print("Cân nặng:", weight, "kg")

print(" --- LOG HỆ THỐNG --- ")
print("Kiểu dữ liệu của patient_name: ", type(patient_name))
print("Kiểu dữ liệu của patient_code: ", type(patient_code))
print("Kiểu dữ liệu của body_temperature: ", type(body_temperature))
print("Kiểu dữ liệu của heart_rate: ", type(heart_rate))
print("Kiểu dữ liệu của weight: ", type(weight))


if isinstance(body_temperature, float) and isinstance(heart_rate, int) and isinstance(weight, float):
    print("Dữ liệu hợp lệ.")
else:
    print("Cảnh báo dữ liệu chưa đúng quy định!")
