cart_items = [
    {"id": "P001", "name": "Điện thoại iPhone 15", "number": 1, "price": 25000000},
    {"id": "P002", "name": "Ốp lưng Silicon", "number": 2, "price": 150000}
]

def view_cart():
    if not cart_items:
        print("Giỏ hàng trống.")
        return
    print("\n--- CHI TIẾT GIỎ HÀNG ---")
    print(f"{'STT':<5}{'Mã SP':<10}{'Tên Sản Phẩm':<25}{'SL':<5}{'Đơn Giá':<15}{'Thành Tiền':<15}")
    total_quantity = 0
    total_price = 0
    for i, item in enumerate(cart_items, start=1):
        total = item["number"] * item["price"]
        total_quantity += item["number"]
        total_price += total
        print(f"{i:<5}{item['id']:<10}{item['name']:<25}{item['number']:<5}{item['price']:<15,}{total:<15,}")
    print(f"\nTổng số lượng: {total_quantity} | Tổng tiền thanh toán: {total_price:,}đ\n")

def add_item():
    id_sp = input("Nhập mã sản phẩm: ").strip()
    name_sp = input("Nhập tên sản phẩm: ").strip()
    try:
        number_sp = int(input("Nhập số lượng: "))
        price_sp = int(input("Nhập đơn giá: "))
        if number_sp <= 0 or price_sp <= 0:
            print("Số lượng hoặc đơn giá phải lớn hơn 0.")
            return
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")
        return

    for item in cart_items:
        if item["id"] == id_sp:
            item["number"] += number_sp
            print("Đã cộng dồn số lượng sản phẩm.")
            return
    cart_items.append({"id": id_sp, "name": name_sp, "number": number_sp, "price": price_sp})
    print("Đã thêm sản phẩm mới vào giỏ hàng.")

def update_item():
    id_sp = input("Nhập mã sản phẩm cần cập nhật: ").strip()
    for item in cart_items:
        if item["id"] == id_sp:
            try:
                new_number = int(input("Nhập số lượng mới: "))
                if new_number <= 0:
                    print("Số lượng phải lớn hơn 0.")
                    return
                item["number"] = new_number
                print("Đã cập nhật số lượng sản phẩm.")
                return
            except ValueError:
                print("Vui lòng nhập số hợp lệ.")
                return
    print("Mã sản phẩm không tồn tại trong giỏ hàng.")

def delete_item():
    id_sp = input("Nhập mã sản phẩm cần xóa: ").strip()
    for item in cart_items:
        if item["id"] == id_sp:
            cart_items.remove(item)
            print("Đã xóa sản phẩm khỏi giỏ hàng.")
            return
    print("Mã sản phẩm không tồn tại trong giỏ hàng.")

def main():
    while True:
        print("\n=== SHOPEE CART MANAGEMENT SYSTEM ===")
        print("1. Xem chi tiết giỏ hàng & Tính tổng tiền")
        print("2. Thêm sản phẩm mới / Cộng dồn số lượng")
        print("3. Cập nhật số lượng sản phẩm")
        print("4. Xóa sản phẩm khỏi giỏ hàng")
        print("5. Thoát chương trình")
        choice = input("Mời bạn chọn chức năng (1-5): ").strip()

        if choice == "1":
            view_cart()
        elif choice == "2":
            add_item()
        elif choice == "3":
            update_item()
        elif choice == "4":
            delete_item()
        elif choice == "5":
            print("Cảm ơn bạn đã sử dụng hệ thống.")
            break
        else:
            print("Vui lòng nhập số từ 1-5.")

if __name__ == "__main__":
    main()
