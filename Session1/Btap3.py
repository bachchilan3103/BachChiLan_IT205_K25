#input:
# name_patient: ho va ten kieu str
# medical_code: id benh nhan str
# department: khoa va phong kham dc chi dinh str
#output: ho ten benh nhan – ma benh – chuyen toi khoa va phog kham

print("=== HỆ THỐNG TIẾP NHẬN BỆNH NHÂN ===")
name_patient = input("Nhập họ và tên bệnh nhân: ")
medical_code = input("Nhập mã bệnh án: ")
department = input("Nhập khoa hay phòng khám chỉ định: ")

print(" --- PHIẾU KHÁM BỆNH ĐIỆN TỬ --- ")
print("Bệnh nhân:", name_patient, end=" – ")
print("Mã bệnh:", medical_code, end=" – ")
print("Chuyển tới:", department)



