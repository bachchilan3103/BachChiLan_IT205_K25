# total_budget dc tao = 0 trong vong lap for thi kh lap
# cach sua: tao total_budget truoc vong lap 
# + them (+=) moi lan nhap luong thay vi gan lai

print(" --- PHẦN MỀM TÍNH TỔNG QUỸ LƯƠNG --- ")
total_budget = 0
for employee_number in range(1, 4):
    print("Dang xu li nvien co ma la", employee_number)
    salary = int(input("Nhap muc luong (VND): "))
    total_budget += salary
print("Tong ngan sach can chuan bi: ", total_budget, "VND")
