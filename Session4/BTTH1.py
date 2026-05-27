# input tong so tieng ban dau cua hoa don int
# output tra ve so tien khach phai tra

total_bill = int(input("Nhap tong tien hoa don ban dau: "))
print(" ---HOA dON THANH TOAN RIKKEI STORE--- ")
sale_price = 0

if total_bill >= 500000:
    sale_price = total_bill * 0.9
else:
    print("Khong dc giam gia")
    sale_price = 0    
    
print("So tien duoc giam: ", sale_price)
print("Tong so tien khach phai tra: ", total_bill - sale_price)
