# chuỗi gdịch thực tế đc phân tách bằng kí tự |
# kh thay đổi trực tiếp biến gốc vì chuỗi trong Python kh the sua
# transaction.split("-") là sai vì delimiter thực tế không phải dấu - mà là |
# tách sai delimiter, danh sách parts chỉ có 1 ptử, nên truy cập parts[1], parts[2] sẽ lỗi
#Cần .strip() lại từng phần sau khi split() để loại bỏ khoảng trắng thừa
# amount chuyển từ chuỗi sang int để có thể định dạng tiền hay tính toán chính xác

transaction = "  nguyEN vAn a | PYTHON-01 | 15000000 | paid  "
transaction = transaction.strip()
parts = transaction.split("|")

student_name = parts[0].strip().title()
course_code = parts[1].strip().upper()
amount = int(parts[2].strip())
status = parts[3].strip().upper()

print("Học viên:", student_name)
print("Khóa học:", course_code)
print("Số tiền:", f"{amount:,} VND")
print("Trạng thái:", status)
