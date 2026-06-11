def main():
    while True:
        print("\n===CLI - Command Line Interface===")
        print("1. Hiển thị nhật kí giao dịch: ")
        print("2. Ghi nhận giao dịch mới: ")
        print("3. Cập nhật chứng từ giao dịch: ")
        print("4. Xóa giao dịch lỗi: ")
        print("5. Tìm kiếm giao dịch: ")
        print("6. Thống kê tổng dòng tiền: ")
        print("7. Phân loại quy mô tự động: ")
        print("8. Thoát chương trình: ")
        choice = input("Mời nhập lựa chọn (1-8): ")
    
    def choice.isdigit():
    choice = int(choice)
        if choice == 1:
            display_transaction_log()
        elif choice == 2:
        elif choice == 3:
        elif choice == 4:
        elif choice == 5:
        elif choice == 6:
        elif choice == 7:
        elif choice == 8:
            print("Thoát chương trình thành công. Hẹn gặp lại.")
            break
        else:
            print("Vui lòng nhập đúng số hợp lệ (1-8): ")
                  
if __main__ == "__main__":
    main()
    