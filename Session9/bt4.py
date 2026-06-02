order_list = [
    "GE001 - PENDING",
    "GE002 - DELIVERING",
    "GE003 - CANCELLED"
]

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS =====")
    print("1. Hiển thị danh sách đơn hàng")
    print("2. Cập nhật danh sách đơn hàng")
    print("3. Thống kê đơn hàng theo trạng thái")
    print("4. Thoát chương trình")
    
    main_choice = input("Mời bạn chọn chức năng (1-4): ")
    
    if main_choice not in ["1", "2", "3", "4"]:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
        continue
        
    if main_choice == "1":
        if len(order_list) == 0:
            print("Danh sách đơn hàng hiện đang trống.")
        else:
            print("Danh sách đơn hàng hiện tại:")
            for index, order in enumerate(order_list, 1):
                print(f"{index}. {order}")
                
    elif main_choice == "2":
        while True:
            print("\n----- CẬP NHẬT DANH SÁCH ĐƠN HÀNG -----")
            print("1. Thêm đơn hàng mới")
            print("2. Sửa đơn hàng theo vị trí")
            print("3. Xóa đơn hàng theo vị trí")
            print("4. Quay lại menu chính")
            
            sub_choice = input("Mời bạn chọn chức năng (1-4): ")
            
            if sub_choice not in ["1", "2", "3", "4"]:
                print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
                continue
                
            if sub_choice == "1":
                code_input = input("Nhập mã đơn hàng: ")
                status_input = input("Nhập trạng thái đơn hàng: ")
                
                clean_code = code_input.strip().upper()
                clean_status = status_input.strip().upper()
                
                new_order = f"{clean_code} - {clean_status}"
                order_list.append(new_order)
                print("Đã thêm đơn hàng mới thành công.")
                
            elif sub_choice == "2":
                pos_input = input("Nhập vị trí đơn hàng cần sửa: ")
                
                if not pos_input.isdigit():
                    print("Vị trí không hợp lệ!")
                    continue
                    
                idx = int(pos_input) - 1
                
                if idx < 0 or idx >= len(order_list):
                    print("Không tồn tại đơn hàng ở vị trí này!")
                    continue
                    
                code_input = input("Nhập mã đơn hàng mới: ")
                status_input = input("Nhập trạng thái đơn hàng mới: ")
                
                clean_code = code_input.strip().upper()
                clean_status = status_input.strip().upper()
                
                order_list[idx] = f"{clean_code} - {clean_status}"
                print("Đã cập nhật đơn hàng thành công.")
                
            elif sub_choice == "3":
                pos_input = input("Nhập vị trí đơn hàng cần xóa: ")
                
                if not pos_input.isdigit():
                    print("Vị trí không hợp lệ!")
                    continue
                    
                idx = int(pos_input) - 1
                
                if idx < 0 or idx >= len(order_list):
                    print("Không tồn tại đơn hàng ở vị trí này!")
                    continue
                    
                removed_order = order_list.pop(idx)
                print(f"Đã xóa đơn hàng: {removed_order}")
                
            elif sub_choice == "4":
                break
                
    elif main_choice == "3":
        pending_count = 0
        delivering_count = 0
        completed_count = 0
        cancelled_count = 0
        
        for order in order_list:
            parts = order.split(" - ")
            if len(parts) == 2:
                status = parts[1]
                if status == "PENDING":
                    pending_count += 1
                elif status == "DELIVERING":
                    delivering_count += 1
                elif status == "COMPLETED":
                    completed_count += 1
                elif status == "CANCELLED":
                    cancelled_count += 1
                    
        print("\n===== THỐNG KÊ ĐƠN HÀNG =====")
        print(f"PENDING: {pending_count}")
        print(f"DELIVERING: {delivering_count}")
        print(f"COMPLETED: {completed_count}")
        print(f"CANCELLED: {cancelled_count}")
        print(f"Tổng số đơn hàng: {len(order_list)}")
        
    elif main_choice == "4":
        print("Thoát chương trình")
        break