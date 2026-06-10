# Dữ liệu mẫu ban đầu
orders = [
    {'id': 'HD01', 'name': 'Đại lý Hoàng Long', 'price': 45000000, 'status': 'Paid'},
    {'id': 'HD02', 'name': 'Tạp hóa Minh Thu', 'price': 15000000, 'status': 'Unpaid'}]

#Hiển thị danh sách đơn hàng
def show_orders(orders):
    if len(orders) == 0:
        print("Danh sách đơn hàng trống!")
    else:
        print(f"{'Mã đơn':<10}{'Tên đại lí':<25}{'Giá trị':>15}{'Trạng thái':>15}")
        print("-" * 65)
        for i in orders:
            print(f"{i['id']:<10}{i['name']:<25}{i['price']:>15,.0f}{i['status']:>15}")
            
#Tạo đơn hàng mới
def create_order(oders):
    id = input("Nhập mã đơn hàng: ").strip()
#Ktra mã có bị trùng kh
    found = False
    for i in orders:
        if i['id'] == id:
            found = True 
            break
    if found:
        print("[ERR-01]: Mã đơn hàng này đã tồn tại")
        return
        
    name = str(input("Nhập tên đại lí: ")).strip()
    price = float(input("Nhập giá đơn hàng(VND): ")).strip()
        
    if price_input.isdigit():
        price = float(price_input)
        if price > 0:
            orders.append({'id': id, 'name': name, 'price': price, 'status': 'Unpaid'})
            print(f"[Thành công]: Đơn hàng {id} đã được tạo mới.")
        else:
            print("[ERR-02]: Giá trị phải lớn hơn 0!")
    else:
        print("[ERR-02]: Vui lòng nhập số hợp lệ!")
        
#Cập nhật trạng thái thanh toán
def update_payment_status(orders):
    id = input("Nhập mã đơn hàng cần cập nhật: ").strip()
    found = False
    for i in orders:
        if i['id'] == id:
            found = True
            if i['status'] == 'Paid':
                print(f"[ERR-04]: Đơn hàng {id} đã thanh toán trước đó!")
            else:
                i['status'] = 'Paid'
                print(f"[Thành công]: Đơn hàng {id} đã được cập nhật trạng thái ĐÃ THANH TOÁN.")
            break
    if not found:
        print(f"[ERR-03]: Không tìm thấy đơn hàng có mã {id}!")

#Tính tổng doanh thu và chiết khấu
def calculate_financials(orders):
    total = 0
    for i in orders:
        if i['status'] == 'Paid':
            total += i['price']

    if total >= 100000000:
        discount_rate = 5
    else:
        discount_rate = 0

    discount_money = total * discount_rate / 100
    return total, discount_rate, discount_money

#Hàm điều phối Menu
def main():
    while True:
        print("\n=== MENU QUẢN LÝ ĐƠN HÀNG ===")
        print("1. Xem danh sách đơn hàng")
        print("2. Tạo mới đơn hàng")
        print("3. Cập nhật trạng thái thanh toán")
        print("4. Tính tổng doanh thu & chiết khấu")
        print("5. Thoát chương trình")
        choice = input("Nhập lựa chọn (1-5): ")

        # Ktra xem người dùng có nhập số không
        if choice.isdigit():
            choice = int(choice)
            if choice == 1:
                show_orders(orders)
            elif choice == 2:
                create_order(orders)
            elif choice == 3:
                update_payment_status(orders)
            elif choice == 4:
                total, rate, discount = calculate_financials(orders)
                print(f"Tổng doanh thu: {total:,.0f} VND")
                print(f"Chiết khấu: {rate}%")
                print(f"Số tiền chiết khấu: {discount:,.0f} VND")
            elif choice == 5:
                print("Cảm ơn bạn đã sử dụng hệ thống. Hẹn gặp lại!")
                break
            else:
                print("[ERR-05]: Lựa chọn không hợp lệ. Vui lòng nhập số từ 1 đến 5.")
        else:
            print("[ERR-05]: Vui lòng chỉ nhập số từ 1 đến 5.")

if __name__ == "__main__":
    main()
