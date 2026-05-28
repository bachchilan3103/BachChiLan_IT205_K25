price_bill = float(input("Nhập đơn giá sản phẩm: "))
quantity = int(input("Nhập số lượng KH mua: "))

total_amount = price_bill * quantity
if total_amount >= 1000000:
    discount = total_amount * 10 / 100
    payment = total_amount - discount
    print("Bạn được giảm giá 10% hóa đơn")
else:
    payment = total_amount
    print("Bạn không được giảm giá")

print("Số tiền cần phải trả là: ", payment)

password_user = "123456"
count = 0

while count < 3:
    password = input("Nhập mật khẩu của bạn: ")
    if password == password_user:
        print("Đăng nhập thành công")
        break
    else:
        count = count + 1
        print("Mật khẩu sai, vui lòng nhập lại")

if count == 3:
    print("Tài khoản đã bị khóa") 
    
total_products = 0
box_valid = 0

while True:
    box_quantity = int(input("Nhập số lượng của từng thùng hàng: "))
    if box_quantity < 0:
        print("Số lượng không hợp lệ, bỏ qua thùng này")
    elif box_quantity == 0:
        break
    else:
        total_products = total_products + box_quantity
        box_valid = box_valid + 1

print("Tổng số thùng hàng hợp lệ đã đếm là: ", box_valid)
print("Tổng số lượng sản phẩm thu được là: ", total_products)    
   
