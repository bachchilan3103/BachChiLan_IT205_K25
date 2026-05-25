import sys

print("--- KHỞI TẠO BỆNH ÁN SỐ ---")
fullname = input("Nhập họ và tên bệnh nhân: ").strip()
age_input = input("Nhập tuổi bệnh nhân: ").strip()

if not age_input.isdigit() and not (age_input.startswith('-') and age_input[1:].isdigit()):
    print("LỖI: Tuổi nhập vào phải là một số nguyên hợp lệ!")
    sys.exit()

age = int(age_input)

if fullname == "":
    print("LỖI: Tên bệnh nhân không được để trống hoặc chỉ chứa khoảng trắng!")
    sys.exit()

if age < 0 or age > 150:
    print("LỖI: Tuổi nằm ngoài phạm vi sinh học của con người (0-150)!")
    sys.exit()

if age < 6:
    triage_result = "ƯU TIÊN: Bệnh nhi - Chuyển thẳng phòng khám Nhi."
elif age >= 80:
    triage_result = "ƯU TIÊN: Người cao tuổi - Hỗ trợ xe lăn, chuyển phòng khám Lão khoa."
else:
    triage_result = "KHÁM THƯỜNG: Vui lòng lấy số thứ tự và chờ tới lượt tại sảnh."

print("\n==================================================")
print("           PHIẾU KHÁM BỆNH ĐIỆN TỬ                ")
print("==================================================")
print(f" Họ và tên: {fullname}")
print(f" Tuổi:      {age}")
print(f" Phân luồng: {triage_result}")
print("==================================================")
