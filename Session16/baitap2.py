# Phân tích lỗi 1:
# Dòng new_prescription = old_prescription không tạo ra list mới.
# Nó chỉ tạo thêm một biến tham chiếu đến cùng vùng nhớ với old_prescription.
# Vì vậy new_prescription và old_prescription thực chất là cùng một list.
# Khi gọi new_prescription.append("Oresol"), phần tử được thêm vào list chung đó,
# nên yesterday_prescription bên ngoài hàm cũng bị thay đổi.

# Các cách tạo bản sao độc lập của list:
# Cách 1: old_prescription.copy()
# Cách 2: old_prescription[:]
# Cách 3: list(old_prescription)
# Cách 4: copy.copy(old_prescription)

# Phân tích lỗi 2:
# String trong Python là immutable (không thể thay đổi trực tiếp).
# Hàm replace() không sửa chuỗi gốc mà trả về một chuỗi mới.
# Dòng:
# new_prescription[0].replace("Panadol", "Paracetamol")
# tạo ra chuỗi mới nhưng không gán lại cho phần tử trong list,
# nên dữ liệu trong danh sách vẫn giữ nguyên là "Panadol".

# Cú pháp đúng:
# new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")

# Sửa code
yesterday_prescription = ["Panadol", "Vitamin C", "Amoxicillin"]

def update_prescription(old_prescription):
    new_prescription = old_prescription.copy()
    new_prescription[0] = new_prescription[0].replace("Panadol", "Paracetamol")
    new_prescription.append("Oresol")
    return new_prescription

today_prescription = update_prescription(yesterday_prescription)

print("Đơn thuốc hôm qua:", yesterday_prescription)
print("Đơn thuốc hôm nay:", today_prescription)
