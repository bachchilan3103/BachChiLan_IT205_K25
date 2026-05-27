total_revenue = 0
invoice_count = 0
large_invoice_count = 0
continue_input = True

while continue_input:
    invoice_value = int(input("Nhap gia tri hoa don: "))
    invoice_count += 1
    total_revenue += invoice_value

    if invoice_value >= 1000000:
        large_invoice_count += 1

    option = input("Muon nhap tiep hay khong y/n: ")
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

print(" BAO CAO DOANH THU CUOI NGAY RIKKEI STORE ")
print("Tong doanh thu:", total_revenue, "VND")
print("Tong so hoa don:", invoice_count, "lon hon 1tr se co", large_invoice_count, "hoa don)")
print("Ti le hoa don lon dat:", round(percentage, 2), "% tren tong so don hang.")