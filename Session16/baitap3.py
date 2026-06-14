# Phân tích lỗi
# Hàm display_patients(patient_list)
# Input:
# - patient_list (list): Danh sách bệnh nhân.
# Output:
# - None.
# Chức năng:
# - Hiển thị toàn bộ danh sách bệnh nhân.
# - Nếu danh sách rỗng thì thông báo không có bệnh nhân.

# Hàm validate_gender(gender_input)
# Input:
# - gender_input (str): Giới tính người dùng nhập.
# Output:
# - True nếu là "nam" hoặc "nu".
# - False nếu dữ liệu không hợp lệ.
# Chức năng:
# - Chuẩn hóa dữ liệu bằng strip() và lower().
# - Kiểm tra giới tính hợp lệ.

# Hàm find_patient_index(patient_list, patient_id)
# Input:
# - patient_list (list): Danh sách bệnh nhân.
# - patient_id (str): Mã bệnh nhân cần tìm.
# Output:
# - Trả về index nếu tìm thấy.
# - Trả về -1 nếu không tìm thấy.
# Chức năng:
# - Tìm kiếm bệnh nhân theo mã.

# Hàm add_patient(patient_list)
# Input:
# - patient_list (list): Danh sách bệnh nhân.
# Output:
# - None.
# Chức năng:
# - Nhập thông tin bệnh nhân mới.
# - Kiểm tra dữ liệu hợp lệ.
# - Chuẩn hóa dữ liệu.
# - Thêm bệnh nhân vào danh sách.

# Hàm update_diagnosis(patient_list)
# Input:
# - patient_list (list): Danh sách bệnh nhân.
# Output:
# - None.
# Chức năng:
# - Tìm bệnh nhân theo mã.
# - Cập nhật chẩn đoán bệnh.

# Hàm search_by_disease(patient_list)
# Input:
# - patient_list (list): Danh sách bệnh nhân.
# Output:
# - None.
# Chức năng:
# - Tìm kiếm bệnh nhân theo tên bệnh.
# - Thống kê số lượng kết quả.

# Mỗi bệnh nhân được lưu dưới dạng:
# ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"]

# Danh sách bệnh nhân được lưu dưới dạng List chứa nhiều List con:
# patients = [
#     ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
#     ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
# ]

# Khi truyền patient_list vào hàm, Python truyền tham chiếu của List.
# Mọi thay đổi bằng append(), cập nhật phần tử,... sẽ tác động trực tiếp lên danh sách gốc.

# Chuẩn hóa mã bệnh nhân:
# patient_id = patient_id.strip().upper()

# Chuẩn hóa tên bệnh nhân:
# patient_name = patient_name.strip().title()

# Chuẩn hóa chẩn đoán bệnh:
# disease = disease.strip().capitalize()

# Tìm kiếm không phân biệt hoa thường:
# keyword.lower() in disease.lower()

# Edge Case 1:
# Kiểm tra trùng mã bệnh nhân bằng find_patient_index().
# Nếu kết quả khác -1 thì mã đã tồn tại.

# Edge Case 2:
# Kiểm tra giới tính bằng validate_gender().
# Chỉ chấp nhận "Nam" hoặc "Nu".

# Edge Case 3:
# Dùng strip() để loại bỏ khoảng trắng.
# Nếu chuỗi rỗng sau strip() thì dữ liệu không hợp lệ.

# Edge Case 4:
# Nếu lựa chọn menu không nằm trong khoảng từ 1 đến 5 thì báo lỗi.

# Triển khai code
patients = [
    ["BN001", "Nguyen Van A", "Nam", "Viem Phoi"],
    ["BN002", "Tran Thi B", "Nu", "Sot Xuat Huyet"]
]

def validate_gender(gender_input):
    return gender_input.strip().lower() in ["nam", "nu"]

def find_patient_index(patient_list, patient_id):
    patient_id = patient_id.strip().upper()
    for i in range(len(patient_list)):
        if patient_list[i][0] == patient_id:
            return i
    return -1

def display_patients(patient_list):
    if len(patient_list) == 0:
        print("Hiện không có bệnh nhân nào đang điều trị.")
        return
    print("----- DANH SÁCH BỆNH NHÂN ĐANG ĐIỀU TRỊ -----")
    for i, patient in enumerate(patient_list, start=1):
        print(f"{i}. Mã: {patient[0]} | Tên: {patient[1]} | Giới tính: {patient[2]} | Bệnh: {patient[3]}")

def add_patient(patient_list):
    print("----- TIẾP NHẬN BỆNH NHÂN MỚI -----")

    patient_id = input("Nhập mã bệnh nhân: ").strip().upper()
    if patient_id == "":
        print("Mã bệnh nhân không được để trống!")
        return

    if find_patient_index(patient_list, patient_id) != -1:
        print("Mã bệnh nhân đã tồn tại trong hệ thống, vui lòng kiểm tra lại!")
        return

    patient_name = input("Nhập tên bệnh nhân: ").strip().title()
    if patient_name == "":
        print("Tên bệnh nhân không được để trống!")
        return

    while True:
        gender = input("Nhập giới tính Nam/Nu: ").strip()
        if validate_gender(gender):
            gender = gender.capitalize()
            break
        print("Giới tính không hợp lệ, vui lòng nhập lại!")

    disease = input("Nhập chẩn đoán bệnh: ").strip().capitalize()

    patient = [patient_id, patient_name, gender, disease]
    patient_list.append(patient)

    print("Tiếp nhận bệnh nhân thành công!")

def update_diagnosis(patient_list):
    print("----- CẬP NHẬT CHẨN ĐOÁN BỆNH -----")

    patient_id = input("Nhập mã bệnh nhân cần cập nhật: ").strip().upper()

    if patient_id == "":
        print("Mã bệnh nhân không được để trống!")
        return

    index = find_patient_index(patient_list, patient_id)

    if index == -1:
        print(f"Không tìm thấy hồ sơ mang mã {patient_id}!")
        return

    print(f"Tìm thấy bệnh nhân: {patient_list[index][1]}")
    print(f"Chẩn đoán hiện tại: {patient_list[index][3]}")

    new_disease = input("Nhập chẩn đoán mới: ").strip()

    if new_disease == "":
        print("Chẩn đoán bệnh không được để trống!")
        return

    patient_list[index][3] = new_disease.capitalize()

    print("Cập nhật chẩn đoán bệnh thành công!")

def search_by_disease(patient_list):
    print("----- TÌM KIẾM BỆNH NHÂN THEO TÊN BỆNH -----")

    keyword = input("Nhập từ khóa tên bệnh: ").strip()

    if keyword == "":
        print("Từ khóa tìm kiếm không được để trống!")
        return

    count = 0

    print("Kết quả tìm kiếm:")

    for patient in patient_list:
        if keyword.lower() in patient[3].lower():
            count += 1
            print(f"{count}. Mã: {patient[0]} | Tên: {patient[1]} | Giới tính: {patient[2]} | Bệnh: {patient[3]}")

    if count == 0:
        print("Không tìm thấy bệnh nhân nào phù hợp.")

    print(f"\nCó tổng cộng {count} bệnh nhân mắc bệnh liên quan đến '{keyword}'.")

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ BỆNH NHÂN RIKKEI =====")
    print("1. Hiển thị danh sách bệnh nhân")
    print("2. Tiếp nhận bệnh nhân mới")
    print("3. Cập nhật chẩn đoán bệnh theo mã BN")
    print("4. Tìm kiếm và thống kê theo tên bệnh")
    print("5. Thoát chương trình")
    print("===========================================")

    choice = input("Nhập lựa chọn của bạn: ").strip()

    if choice == "1":
        display_patients(patients)
    elif choice == "2":
        add_patient(patients)
    elif choice == "3":
        update_diagnosis(patients)
    elif choice == "4":
        search_by_disease(patients)
    elif choice == "5":
        print("Cảm ơn bác sĩ đã sử dụng hệ thống!")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập số từ 1-5!")
