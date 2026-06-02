username = ""
title = ""
description = ""
hashtags = []

while True:
    print("\n--- HỆ THỐNG KIỂM DUYỆT NỘI DUNG TIKTOK ---")
    print("1. Nhập dữ liệu và xem báo cáo thống kê")
    print("2. Chuẩn hóa tên tài khoản TikTok")
    print("3. Kiểm tra hashtag hợp lệ")
    print("4. Tìm kiếm và thay thế từ khóa trong mô tả")
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
        username_input = input("Nhập tên tài khoản người đăng: ")
        if username_input.strip() == "":
            print("Lỗi: Tên tài khoản không được rỗng!")
            continue
            
        title_input = input("Nhập tiêu đề video: ")
        
        description_input = input("Nhập mô tả video: ")
        if description_input.strip() == "":
            print("Lỗi: Mô tả video không được rỗng!")
            continue
            
        hashtag_input = input("Nhập danh sách hashtag (cách nhau bởi dấu phẩy): ")
        
        username = username_input.strip()
        title = title_input.strip().title()
        description = description_input.strip()
        
        raw_hashtags = hashtag_input.split(",")
        hashtags = []
        for tag in raw_hashtags:
            clean_tag = tag.strip()
            if clean_tag != "":
                hashtags.append(clean_tag)
                
        word_count = len(description.split())
        
        print("\n--- BÁO CÁO THỐNG KÊ VIDEO ---")
        print("Tên tài khoản:", username)
        print("Tiêu đề video:", title)
        print("Mô tả video:", description)
        print("Độ dài mô tả video (số ký tự):", len(description))
        print("Số lượng từ trong mô tả:", word_count)
        print("Danh sách hashtag:", hashtags)
        print("Số lượng hashtag:", len(hashtags))
        print("Mô tả viết thường:", description.lower())
        print("Mô tả viết hoa:", description.upper())
        
    elif choice == 2:
        if username == "":
            print("Vui lòng chạy chức năng 1 để nhập tên tài khoản trước!")
        else:
            username_lower = username.lower()
            normalized_username = "@" + username_lower
            print("Tên tài khoản ban đầu:", username)
            print("Tên tài khoản sau khi chuẩn hoá:", normalized_username)
            
    elif choice == 3:
        new_hashtag = input("Nhập một hashtag cần kiểm tra: ")
        
        if new_hashtag == "":
            print("Lý do không hợp lệ: Hashtag không được rỗng!")
        elif not new_hashtag.startswith("#"):
            print("Lý do không hợp lệ: Hashtag phải bắt đầu bằng ký tự #!")
        elif " " in new_hashtag:
            print("Lý do không hợp lệ: Hashtag không được chứa khoảng trắng!")
        elif len(new_hashtag) < 2:
            print("Lý do không hợp lệ: Hashtag phải có ít nhất 2 ký tự!")
        else:
            content_after_hash = new_hashtag[1:]
            is_valid = True
            for char in content_after_hash:
                if not (char.isalnum() or char == "_"):
                    is_valid = False
                    break
            
            if is_valid:
                print("Hashtag hợp lệ!")
                hashtags.append(new_hashtag)
                print("Danh sách hashtag hiện tại sau khi thêm:", hashtags)
            else:
                print("Lý do không hợp lệ: Hashtag chỉ nên chứa chữ cái, chữ số hoặc dấu gạch dưới!")
                
    elif choice == 4:
        if description == "":
            print("Vui lòng chạy chức năng 1 để nhập mô tả video trước!")
        else:
            search_word = input("Nhập từ khóa cần tìm: ")
            replace_word = input("Nhập từ khóa thay thế: ")
            
            if search_word in description:
                occurrence = description.count(search_word)
                description = description.replace(search_word, replace_word)
                print("Tìm thấy từ khóa!")
                print("Số lần từ khóa xuất hiện trong mô tả:", occurrence)
                print("Mô tả video sau khi thay thế:", description)
            else:
                print("Không tìm thấy từ khóa cần tìm trong mô tả video.")
                
    elif choice == 5:
        print("Thoát chương trình")
        break