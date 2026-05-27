# input nhap gtri hoa don cua tung khach hang
# nhap lua chon tiep hay khong
# total_bill, count_bill = 0 
# output tong doanh thu, tong so hoa don, so hoa don > 1tr
# % cua nhom hdon lon tren tog so hdon da ban dc

total_bill = 0
count_bill = 0
target_bill = 0
continue_input = True

while continue_input:
    invoice_value = float(input("Nhap gtri hoa don: "))
    invoice_count += 1
    total_revenue += invoice_value

    if invoice_value >= 1000000:
        large_invoice_count += 1

    option = input("Nhap y de tiep hoac n kthuc: ")
    if option == "n" or option == "N":
        continue_input = False
    elif option == "y" or option == "Y":
        continue_input = True
        
if invoice_count == 0:
    total_revenue = 0
    large_invoice_count = 0
    percentage = 0
else:
    percentage = (large_invoice_count / invoice_count) * 100

print("Tong doanh thu:", total_revenue)
print("Tong so hoa don:", invoice_count)
print("So hoa don > 1tr:", large_invoice_count)
print("Ti le phan tram hoa don:", round(percentage, 2), "%")