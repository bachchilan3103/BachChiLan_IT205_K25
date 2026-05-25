# patient_name: ho ten str
# patient_code: ma benh nhan str
# body_temperature: nhiet do co the float
# heart_rate: nhip tim int
# weight: can nag float

import random  
print(" === TIẾP NHẬN THÔNG TIN BỆNH NHÂN === ")
name = str(input("Nhập tên bệnh nhân: "))
gender = str(input("Nhập giới tính: "))
year_of_birth = int(input("Nhập năm sinh: "))
phone = str(input("Nhập số điện thoại: "))
email = str(input("Nhập email: "))
symptom = str(input("Nhập triệu chứng ban đầu: "))
cost = float(input("Nhập chi phí khám: "))    
random_code = random.randint(100, 999) 
patient_code = f"BN{year_of_birth}{random_code}"

print(" --- THẺ BỆNH NHÂN ---")
print("Mã BN: ", patient_code)
print("Tên: ", name, type(name))
print("Giới tính: ", gender, type(gender))
print("Năm sinh: ", year_of_birth, type(year_of_birth))
print("Điện thoại: ", phone, type(phone))
print("Email: ", email, type(email))
print("Triệu chứng: ", symptom, type(symptom))
print("Chi phí: ", cost, type(cost))

if type(year_of_birth) == int and type(cost) == float:
    print("Dữ liệu hợp lệ.")
else:
    print("Cảnh báo dữ liệu chưa đúng!")




