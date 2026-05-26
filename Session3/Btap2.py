# Nvien co ngay cong lon hon 0 thi dc thuong
# Nvien co ngay cong =0 kh dc thuong va bi email cbao
# days_worked = 0 ctrinh van chay dong gui email chuc mung dan den kqua sai

print(" -THƯỞNG QUÀ EMAIL THƯỞNG TẾT- ")
for employee_number in range(1, 4):
    days_worked = int(input("Nhap so ngay cong: "))
    if days_worked > 0:
        bonus_amount = days_worked * 200000
        print(f"Chuc mung nhan vien {employee_number} dc {bonus_amount} VNĐ tien thuong!")
    else:
        print(f"Nhan vien {employee_number} nghi ca thang, kh dc thuong. Gui email cbao.")
