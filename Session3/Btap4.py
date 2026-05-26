# Input nhap so luong nhan su moi trong thang int
# Output neu nhap <= 0 se bao loi va ycau nhap lai
# nhap > 0 thi in tbao ghi nhan tcong

while True:
    new_employees = int(input("Vui long nhap so luong nhan su moi trong thang: "))
    if new_employees <= 0:
        print("So luong kh hop le ban chi dc nhap so duong!\n")
    else:
        print(f"Ghi nhan ycau cap phat tai san cho {new_employees} nsu moi!\n")
        print("-- CHUONG TRINH KET THUC --")
        break
