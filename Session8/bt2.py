shop_name = ""
product_name = ""
description = ""
category = ""
keywords = []
vouchers = []

while True:
    print("\n--- HỆ THỐNG KIỂM DUYỆT NỘI DUNG SẢN PHẨM SHOPEE ---")
    print("1. Nhập dữ liệu sản phẩm và xem báo cáo thống kê")
    print("2. Chuẩn hóa tên Shop")
    print("3. Kiểm tra mã giảm giá hợp lệ")
    print("4. Tìm kiếm và thay thế từ khóa trong mô tả sản phẩm")
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
        shop_input = input("Nhập tên shop: ")
        if shop_input.strip() == "":
            print("Tên shop không được bỏ trống")
            continue
            
        product_input = input("Nhập tên sản phẩm: ")
        
        description_input = input("Nhập mô tả sản phẩm: ")
        if description_input.strip() == "":
            print("Mô tả sản phẩm không được rỗng")
            continue
            
        category_input = input("Nhập danh mục sản phẩm: ")
        keyword_input = input("Nhập danh sách từ khóa tìm kiếm (cách nhau bởi dấu phẩy): ")
        
        shop_name = shop_input.strip()
        product_name = product_input.strip().title()
        description = description_input.strip()
        category = category_input.strip().lower()
        
        raw_keywords = keyword_input.split(",")
        keywords = []
        for kw in raw_keywords:
            clean_kw = kw.strip()
            if clean_kw != "":
                keywords.append(clean_kw)
                
        print("\n--- BÁO CÁO THỐNG KÊ SẢN PHẨM ---")
        print("Tên shop:", shop_name)
        print("Tên sản phẩm:", product_name)
        print("Mô tả sản phẩm:", description)
        print("Độ dài mô tả sản phẩm:", len(description))
        print("Danh mục sản phẩm:", category)
        print("Danh sách từ khóa:", keywords)
        print("Số lượng từ khóa tìm kiếm:", len(keywords))
        print("Mô tả viết thường:", description.lower())
        print("Mô tả viết hoa:", description.upper())
        
    elif choice == 2:
        if shop_name == "":
            print("Vui lòng chạy chức năng 1 để nhập tên shop trước!")
        else:
            clean_shop = shop_name.lower()
            clean_shop = "-".join(clean_shop.split())
            if not clean_shop.startswith("shop-"):
                clean_shop = "shop-" + clean_shop
            print("Tên shop ban đầu:", shop_name)
            print("Tên shop sau khi được chuẩn hóa:", clean_shop)
            
    elif choice == 3:
        voucher_code = input("Nhập mã giảm giá cần kiểm tra: ")
        
        if voucher_code == "":
            print("Lý do không hợp lệ: Mã giảm giá không được rỗng!")
        elif " " in voucher_code:
            print("Lý do không hợp lệ: Mã giảm giá không được chứa khoảng trắng!")
        elif len(voucher_code) < 6 or len(voucher_code) > 12:
            print("Lý do không hợp lệ: Mã giảm giá phải có độ dài từ 6 đến 12 ký tự!")
        elif not voucher_code.isupper():
            print("Lý do không hợp lệ: Mã giảm giá phải được viết hoa toàn bộ!")
        elif not voucher_code.isalnum():
            print("Lý do không hợp lệ: Mã giảm giá chỉ được chứa chữ cái và chữ số!")
        elif not voucher_code.startswith("SALE"):
            print("Lý do không hợp lệ: Mã giảm giá phải bắt đầu bằng chuỗi SALE!")
        else:
            print("Mã giảm giá hợp lệ")
            vouchers.append(voucher_code)
            print("Danh sách mã giảm giá hiện tại:", vouchers)
            
    elif choice == 4:
        if description == "":
            print("Vui lòng chạy chức năng 1 để nhập mô tả sản phẩm trước!")
        else:
            search_word = input("Nhập từ khóa cần tìm: ")
            replace_word = input("Nhập từ khóa thay thế: ")
            
            if search_word in description:
                occurrence = description.count(search_word)
                description = description.replace(search_word, replace_word)
                print("Số lần xuất hiện của từ khóa:", occurrence)
                print("Mô tả sau khi thay thế:", description)
            else:
                print("Không tìm thấy từ khóa cần tìm trong mô tả sản phẩm.")
                
    elif choice == 5:
        print("Thoát chương trình")
        break