# input
# code_patient: ma benh nhan str
# temperature: Than nhiet float
# heart_rate: nhip tim int

print(" === KẾT QUẢ CHUẨN HÓA DỮ LIỆU === ")
code_patient = input("Nhập mã bệnh nhân: ")
temperature = float(input("Nhập nhiệt độ: "))
heart_rate = int(input("Nhập nhịp tim: "))

print("Mã bệnh nhân:", code_patient)
print("Nhiệt độ cơ thể:", temperature, "C")
print("Kiểu dữ liệu hệ thống:", type(temperature))
print("Nhịp tim:", heart_rate, "nhịp")
print("Kiểu dữ liệu hệ thống:", type(heart_rate))

if isinstance(temperature, float) and isinstance(heart_rate, int):
    print("Thông báo dữ liệu hợp")
else:
    print("Cảnh báo dữ liệu chưa đúng!")
