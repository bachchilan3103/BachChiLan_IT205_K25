total_bill = int(input("Nhap so luong hoa don trong ca: "))
value_bill = int(input(f"Nhap gia tri hoa don thu 1: "))

max_bill = value_bill
min_bill = value_bill
for i in range(2, total_bill + 1):
    value_bill = int(input(f"Nhap gia tri hoa don thu {i}: "))
    
    if value_bill > max_bill:
        max_bill = value_bill
        
    if value_bill < min_bill:
        min_bill = value_bill
        
print("-- KET QUA KIEM TOAN CA RIKKEI STORE --")
print("Hoa don co gia tri cao nhat: ", max_bill,"VND")
print("Hoa don co gia tri thap nhat: ", min_bill,"VND")

