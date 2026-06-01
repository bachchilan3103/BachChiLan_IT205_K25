# các phương thức chuỗi như strip,title,upper,lower 
# kh thay đổi trực tiếp biến gốc vì chuỗi trong Python kh the sua
# mỗi phương thức sẽ trả về 1 chuỗi mới đã được xử lý 
# nếu không gán lại cho biến, giá trị cũ vẫn giữ nguyên

student_name = "  nguYEn vAn a   "
student_code = " rk-001-python "
email = " student01@gamil.com "


student_name = student_name.strip().title()
student_code = student_code.strip().upper()
email = email.strip().lower()

print("Họ tên:", student_name)
print("Mã học viên:", student_code)
print("Email:", email)
