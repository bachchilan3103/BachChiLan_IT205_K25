# Phân tích lỗi
# Danh sách chẩn đoán hiện tại của bệnh nhân Nguyễn Văn A
# patient_diagnoses = ["Sốt Xuất Huyết"]

# Hàm chuẩn hóa tên bệnh và thêm vào hồ sơ
# def add_diagnosis(raw_diagnosis, current_list):

    # Lỗi:
    # String trong Python là immutable (bất biến).
    # Hàm strip() không thay đổi trực tiếp chuỗi gốc.
    # Nó tạo ra một chuỗi mới đã được loại bỏ khoảng trắng đầu/cuối.
    # Do không gán lại nên kết quả bị bỏ đi.
    # raw_diagnosis.strip()

    # Lỗi:
    # title() cũng trả về một chuỗi mới với chữ cái đầu mỗi từ được viết hoa.
    # Vì không gán lại nên raw_diagnosis vẫn giữ nguyên giá trị ban đầu:
    # "  viEm phE QUan  "
    # raw_diagnosis.title()

    # Lỗi:
    # extend() thêm từng phần tử của iterable vào list.
    # String là một iterable gồm nhiều ký tự.
    # Dòng lệnh này tương đương với việc thêm lần lượt:
    # ' ', ' ', 'v', 'i', 'E', 'm', ...
    # vào danh sách bệnh án.
    # current_list.extend(raw_diagnosis)

    # Trả về danh sách sau khi bị thêm từng ký tự rời rạc.
    # return current_list

# Bác sĩ nhập thêm một chẩn đoán mới bị lỗi định dạng.
# new_diagnosis = "  viEm phE QUan  "

# Gọi hàm xử lý.
# updated_diagnoses = add_diagnosis(new_diagnosis, patient_diagnoses)

# Kết quả sai:
# ['Sốt Xuất Huyết', ' ', ' ', 'v', 'i', 'E', 'm', ...]
# print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)

# Sửa code
patient_diagnoses = ["Sốt Xuất Huyết"]

def add_diagnosis(raw_diagnosis, current_list):
    raw_diagnosis = raw_diagnosis.strip().title()
    current_list.append(raw_diagnosis)
    return current_list

new_diagnosis = "  viEm phE QUan  "

updated_diagnoses = add_diagnosis(new_diagnosis, patient_diagnoses)

print("Hồ sơ bệnh án (Các chẩn đoán):", updated_diagnoses)
