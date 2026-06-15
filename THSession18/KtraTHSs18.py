inventory = [
    {'id': 'G01', 'name': 'Gạo tẻ', 'quantity': 50},
    {'id': 'G02', 'name': 'Mì tôm', 'quantity': 120}
]

def show_inventory(inventory_list):
    if len(inventory_list) == 0:
        print("Kho hàng hiện đang trống!")
    else:
        print(f"{'ID':<10}{'Tên hàng hóa':<25}{'Số lượng tồn':>15}")
        print("-" * 50)
        for item in inventory_list:
            print(f"{item['id']:<10}"f"{item['name']:<25}"f"{item['quantity']:>15}")

def main():
    while True:
        print("\n============================")
        print("QUẢN LÝ KHO HÀNG - GROCERY STORE")
        print("============================")
        print("1. Xem danh sách hàng tồn kho")
        print("2. Nhập thêm hàng hóa mới")
        print("3. Cập nhật số lượng tồn kho")
        print("4. Thoát chương trình")
        print("============================")

        choice = input("Nhập lựa chọn (1-4): ")

        if choice == "1":
            show_inventory(inventory)
        elif choice == "2":
            add_item(inventory)
        elif choice == "4":
            print("Cảm ơn vì đã sử dụng hệ thống. Hẹn gặp lại!")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng nhập từ (1-4).")

if __name__ == "__main__":
    main()