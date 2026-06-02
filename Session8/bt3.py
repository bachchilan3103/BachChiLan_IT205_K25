sender_name = ""
sender_phone = ""
pickup_address = ""
receiver_name = ""
receiver_phone = ""
delivery_address = ""
delivery_note = ""

while True:
    print("\n--- HỆ THỐNG QUẢN LÝ ĐƠN HÀNG GRAB EXPRESS ---")
    print("1. Nhập dữ liệu đơn hàng và xem báo cáo thống kê")
    print("2. Chuẩn hóa mã đơn hàng")
    print("3. Ẩn số điện thoại khách hàng")
    print("4. Tìm kiếm và thay thế từ khóa trong ghi chú giao hàng")
    print("5. Thoát chương trình")
    
    choice_input = input("Mời bạn chọn chức năng (1-5): ")
    
    if not choice_input.isdigit():
        print("Lỗi: Lựa chọn không hợp lệ. Vui lòng nhập lại một số từ 1 đến 5!")
        continue
        
    choice = int(choice_input)
    
    if choice < 1 or choice > 5:
        print("Lỗi: Lựa chọn không nằm trong khoảng 1 đến 5. Vui lòng nhập lại!")
        continue
        
    if choice == 1:
        s_name = input("Nhập tên người gửi: ")
        if s_name.strip() == "":
            print("Tên người gửi không được bỏ trống")
            continue
            
        s_phone = input("Nhập số điện thoại người gửi: ")
        if s_phone.strip() == "":
            print("Số điện thoại người gửi không được bỏ trống")
            continue
            
        p_address = input("Nhập địa chỉ lấy hàng: ")
        if p_address.strip() == "":
            print("Địa chỉ lấy hàng không được bỏ trống")
            continue
            
        r_name = input("Nhập tên người nhận: ")
        if r_name.strip() == "":
            print("Tên người nhận không được bỏ trống")
            continue
            
        r_phone = input("Nhập số điện thoại người nhận: ")
        if r_phone.strip() == "":
            print("Số điện thoại người nhận không được bỏ trống")
            continue
            
        d_address = input("Nhập địa chỉ giao hàng: ")
        if d_address.strip() == "":
            print("Địa chỉ giao hàng không được bỏ trống")
            continue
            
        d_note = input("Nhập ghi chú giao hàng: ")
        if d_note.strip() == "":
            print("Ghi chú giao hàng không được bỏ trống")
            continue
            
        sender_name = s_name.strip().title()
        sender_phone = s_phone.strip()
        pickup_address = " ".join(p_address.split())
        receiver_name = r_name.strip().title()
        receiver_phone = r_phone.strip()
        delivery_address = " ".join(d_address.split())
        delivery_note = d_note.strip()
        
        print("\n--- BÁO CÁO THỐNG KÊ ĐƠN HÀNG ---")
        print("Tên người gửi:", sender_name)
        print("Tên người nhận:", receiver_name)
        print("Địa chỉ lấy hàng:", pickup_address)
        print("Địa chỉ giao hàng:", delivery_address)
        print("Ghi chú giao hàng:", delivery_note)
        print("Độ dài ghi chú giao hàng:", len(delivery_note))
        print("Số lượng từ trong ghi chú giao hàng:", len(delivery_note.split()))
        print("Ghi chú dạng chữ thường:", delivery_note.lower())
        print("Ghi chú dạng chữ hoa:", delivery_note.upper())
        
    elif choice == 2:
        order_code = input("Nhập mã đơn hàng cần chuẩn hóa: ")
        if order_code.strip() == "":
            print("Mã đơn hàng không được bỏ trống")
            continue
            
        clean_code = order_code.strip().upper()
        clean_code = "-".join(clean_code.split())
        
        if not clean_code.startswith("GRAB-"):
            clean_code = "GRAB-" + clean_code
            
        print("Mã đơn hàng ban đầu:", order_code)
        print("Mã đơn hàng sau khi được chuẩn hóa:", clean_code)
        
    elif choice == 3:
        if sender_phone == "" or receiver_phone == "":
            print("Vui lòng chạy chức năng 1 để nhập thông tin đơn hàng trước!")
            continue
            
        if not (sender_phone.isdigit() and len(sender_phone) == 10):
            print("Số điện thoại người gửi không hợp lệ: Phải có đúng 10 ký tự số!")
            continue
            
        if not (receiver_phone.isdigit() and len(receiver_phone) == 10):
            print("Số điện thoại người nhận không hợp lệ: Phải có đúng 10 ký tự số!")
            continue
            
        hidden_sender = sender_phone[:3] + "*****" + sender_phone[-2:]
        hidden_receiver = receiver_phone[:3] + "*****" + receiver_phone[-2:]
        
        print("SĐT người gửi:", hidden_sender)
        print("SĐT người nhận:", hidden_receiver)
        
    elif choice == 4:
        if delivery_note == "":
            print("Chưa có ghi chú giao hàng để tìm kiếm")
            continue
            
        search_word = input("Nhập từ khóa cần tìm: ")
        replace_word = input("Nhập từ khóa thay thế: ")
        
        if search_word in delivery_note:
            occurrence = delivery_note.count(search_word)
            delivery_note = delivery_note.replace(search_word, replace_word)
            print("Số lần xuất hiện của từ khóa:", occurrence)
            print("Ghi chú đơn hàng sau khi thay thế:", delivery_note)
        else:
            print("Không tìm thấy từ khóa cần tìm trong ghi chú giao hàng.")
            
    elif choice == 5:
        print("Thoát chương trình")
        break