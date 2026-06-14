# Phân tích lỗi
# Hàm display_records(records)
# Input:
# - records (list): Danh sách hồ sơ bệnh án.
# Output:
# - None.
# Chức năng:
# - Hiển thị toàn bộ hồ sơ bệnh nhân.
# - Tách chuỗi bằng split("-") để lấy thông tin.

# Hàm find_patient_index(records, patient_id)
# Input:
# - records (list): Danh sách hồ sơ bệnh án.
# - patient_id (str): Mã bệnh nhân cần tìm.
# Output:
# - Trả về index nếu tìm thấy.
# - Trả về -1 nếu không tìm thấy.
# Chức năng:
# - Duyệt danh sách.
# - Tách chuỗi lấy mã bệnh nhân.
# - So sánh với mã cần tìm.

# Hàm add_patient(records)
# Input:
# - records (list): Danh sách hồ sơ bệnh án.
# Output:
# - None.
# Chức năng:
# - Nhập thông tin bệnh nhân mới.
# - Kiểm tra trùng mã.
# - Kiểm tra năm sinh hợp lệ.
# - Chuẩn hóa dữ liệu.
# - Ghép dữ liệu bằng join().
# - Thêm hồ sơ vào danh sách.

# Hàm update_diagnosis(records)
# Input:
# - records (list): Danh sách hồ sơ bệnh án.
# Output:
# - None.
# Chức năng:
# - Tìm bệnh nhân theo mã.
# - Nhập chẩn đoán mới.
# - Tách chuỗi thành list.
# - Cập nhật phần tử cuối.
# - Ghép lại thành chuỗi mới.
# - Gán đè vào danh sách.

# Hàm generate_age_report(records)
# Input:
# - records (list): Danh sách hồ sơ bệnh án.
# Output:
# - None.
# Chức năng:
# - Tính tuổi từng bệnh nhân.
# - Phân loại theo nhóm tuổi.
# - Thống kê số lượng từng nhóm.

# Dữ liệu được lưu dưới dạng chuỗi:
# "BN001-Nguyen Van A-1985-Viem Phoi"

# Khi cần lấy thông tin:
# parts = record.split("-")

# Khi cần tạo hồ sơ mới:
# record = "-".join([patient_id, name, birth_year, diagnosis])

# String là immutable.
# Không thể sửa trực tiếp một phần của chuỗi.

# Muốn cập nhật chẩn đoán:
# - split() thành list.
# - sửa phần tử cần thay đổi.
# - join() thành chuỗi mới.
# - gán lại vào danh sách.

# Edge Case 1:
# Năm sinh phải là số.
# Dùng isdigit() kiểm tra.

# Edge Case 2:
# Năm sinh phải nằm trong khoảng từ 1900 đến năm hiện tại.

# Edge Case 3:
# Kiểm tra trùng mã bệnh nhân bằng startswith()
# hoặc hàm find_patient_index().

# Edge Case 4:
# Nếu không tìm thấy mã bệnh nhân thì thông báo lỗi.

# Edge Case 5:
# Nếu tên hoặc chẩn đoán chứa dấu "-"
# thì thay bằng khoảng trắng trước khi lưu.

patient_records = [
    "BN001-Nguyen Van A-1985-Viem Phoi",
    "BN002-Tran Thi B-1990-Sot Xuat Huyet",
    "BN003-Le Van C-2015-Viem Phe Quan"
]

def find_patient_index(records, patient_id):
    patient_id = patient_id.strip().upper()

    for i in range(len(records)):
        if records[i].startswith(patient_id + "-"):
            return i

    return -1

def display_records(records):
    if len(records) == 0:
        print("Hệ thống hiện chưa có hồ sơ nào.")
        return

    print("--- DANH SÁCH BỆNH NHÂN --------------------------------------------------")

    for i in range(len(records)):
        patient_id, name, birth_year, diagnosis = records[i].split("-")
        print(f"{i + 1}. [{patient_id}] {name:<18} | Năm sinh: {birth_year} | Chẩn đoán: {diagnosis}")

    print("--------------------------------------------------------------------------")

def add_patient(records):
    print("\n--- THÊM HỒ SƠ BỆNH NHÂN MỚI ---")

    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()

    if find_patient_index(records, patient_id) != -1:
        print("\nMã bệnh nhân đã tồn tại!")
        return

    name = input("Nhập tên bệnh nhân: ").strip()
    name = name.replace("-", " ").title()

    while True:
        birth_year = input("Nhập năm sinh: ").strip()

        if not birth_year.isdigit():
            print("\nNăm sinh không hợp lệ, vui lòng nhập lại!")
            continue

        if int(birth_year) < 1900 or int(birth_year) > 2026:
            print("\nNăm sinh không hợp lệ, vui lòng nhập lại!")
            continue

        break

    diagnosis = input("Nhập chẩn đoán: ").strip()
    diagnosis = diagnosis.replace("-", " ").capitalize()

    record = "-".join([patient_id, name, birth_year, diagnosis])

    records.append(record)

    print("\nThêm hồ sơ bệnh nhân thành công!")

def update_diagnosis(records):
    print("\n--- CẬP NHẬT CHẨN ĐOÁN THEO MÃ BN ---")

    patient_id = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()

    index = find_patient_index(records, patient_id)

    if index == -1:
        print(f"\nKhông tìm thấy bệnh nhân mang mã {patient_id}!")
        return

    data = records[index].split("-")

    print(f"\nTìm thấy bệnh nhân: {data[1]}")
    print(f"Chẩn đoán hiện tại: {data[3]}")

    new_diagnosis = input("Nhập chẩn đoán mới: ").strip()
    new_diagnosis = new_diagnosis.replace("-", " ").capitalize()

    data[3] = new_diagnosis

    records[index] = "-".join(data)

    print("\nCập nhật chẩn đoán thành công!")

def generate_age_report(records):
    children = 0
    adults = 0
    elderly = 0

    for record in records:
        data = record.split("-")
        age = 2026 - int(data[2])

        if age < 16:
            children += 1
        elif age <= 60:
            adults += 1
        else:
            elderly += 1

    print("\n--- BÁO CÁO PHÂN LOẠI THEO ĐỘ TUỔI ---")
    print(f"Trẻ em: {children} bệnh nhân")
    print(f"Trưởng thành: {adults} bệnh nhân")
    print(f"Người cao tuổi: {elderly} bệnh nhân")
    print("--------------------------------------")

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ BỆNH ÁN RIKKEI HOSPITAL =====")
    print("1. Xem danh sách hồ sơ bệnh án")
    print("2. Thêm hồ sơ bệnh nhân mới")
    print("3. Cập nhật chẩn đoán theo Mã BN")
    print("4. Báo cáo phân loại theo độ tuổi")
    print("5. Thoát chương trình")
    print("==================================================")

    choice = input("Chọn chức năng (1-5): ").strip()

    if choice == "1":
        display_records(patient_records)
    elif choice == "2":
        add_patient(patient_records)
    elif choice == "3":
        update_diagnosis(patient_records)
    elif choice == "4":
        generate_age_report(patient_records)
    elif choice == "5":
        print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập từ 1 đến 5!")
