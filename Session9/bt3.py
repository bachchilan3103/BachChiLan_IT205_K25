order_list = ["GE001", "GE002", "GE003"]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Thêm đơn hàng mới")
    print("3. Xóa đơn hàng theo mã")
    print("4. Thoát chương trình")
    
    choice = input("Mời bạn chọn chức năng (1-4): ")
    
    if choice not in ["1", "2", "3", "4"]:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue
        
    if choice == "1":
        if len(order_list) == 0:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("Danh sách đơn hàng hiện tại:")
            for index, order in enumerate(order_list, 1):
                print(f"{index}. {order}")
                
    elif choice == "2":
        new_order = input("Nhập mã đơn hàng mới: ")
        clean_order = new_order.strip().upper()
        
        if clean_order == "":
            print("Lỗi: Mã đơn hàng không được để trống!")
        else:
            order_list.append(clean_order)
            print(f"Đã thêm đơn hàng {clean_order} vào hệ thống.")
            
    elif choice == "3":
        delete_order = input("Nhập mã đơn hàng cần xóa: ")
        clean_delete_order = delete_order.strip().upper()
        
        if clean_delete_order in order_list:
            order_list.remove(clean_delete_order)
            print(f"Đã xóa thành công đơn hàng {clean_delete_order}.")
        else:
            print("Không tìm thấy mã đơn hàng cần xóa!")
            
    elif choice == "4":
        print("Thoát chương trình.")
        break