saving_accounts = [
    {
        "account_id": "100004",
        "customer_name": "Nguyễn Văn A",
        "customer_code": "KH001",
        "balance": 50000000,
        "interest_rate": 0.05,
        "account_status": "active"
    },
    {
        "account_id": "100005",
        "customer_name": "Trần Thị B",
        "customer_code": "KH002",
        "balance": 20000000,
        "interest_rate": 0.04,
        "account_status": "active"
    }
]

def view_accounts():
    if not saving_accounts:
        print("📂 Không có sổ tiết kiệm nào trong hệ thống.")
        return
    print("\n--- DANH SÁCH SỔ TIẾT KIỆM ---")
    print(f"{'Mã Sổ':<10}{'Tên Khách Hàng':<20}{'Mã KH':<10}{'Số Dư':<15}{'Lãi Suất':<10}{'Trạng Thái':<10}")
    for acc in saving_accounts:
        print(f"{acc['account_id']:<10}{acc['customer_name']:<20}{acc['customer_code']:<10}{acc['balance']:<15,}{acc['interest_rate']:<10}{acc['account_status']:<10}")
    print()

def open_account():
    account_id = input("Nhập mã sổ tiết kiệm: ").strip()
    customer_name = input("Nhập tên khách hàng: ").strip()
    customer_code = input("Nhập mã khách hàng: ").strip()
    try:
        balance = int(input("Nhập số tiền gửi ban đầu: "))
        interest_rate = float(input("Nhập lãi suất (%): "))
        if balance <= 0 or interest_rate <= 0:
            print("Số tiền gửi và lãi suất phải lớn hơn 0.")
            return
    except ValueError:
        print("Vui lòng nhập số hợp lệ.")
        return

    saving_accounts.append({
        "account_id": account_id,
        "customer_name": customer_name,
        "customer_code": customer_code,
        "balance": balance,
        "interest_rate": interest_rate,
        "account_status": "active"
    })
    print("Đã mở sổ tiết kiệm mới thành công.")

def update_account():
    account_id = input("Nhập mã sổ tiết kiệm cần cập nhật: ").strip()
    for acc in saving_accounts:
        if acc["account_id"] == account_id:
            try:
                new_balance = int(input("Nhập số dư mới: "))
                new_rate = float(input("Nhập lãi suất mới (%): "))
                acc["balance"] = new_balance
                acc["interest_rate"] = new_rate
                print("✅ Đã cập nhật thông tin sổ tiết kiệm.")
                return
            except ValueError:
                print("Vui lòng nhập số hợp lệ.")
                return
    print("Mã sổ tiết kiệm không tồn tại.")

def close_account():
    account_id = input("Nhập mã sổ tiết kiệm cần tất toán: ").strip()
    for acc in saving_accounts:
        if acc["account_id"] == account_id:
            if acc["account_status"] == "closed":
                print("Sổ tiết kiệm này đã được tất toán trước đó.")
                return
            acc["account_status"] = "closed"
            print("Đã tất toán sổ tiết kiệm thành công.")
            return
    print("Mã sổ tiết kiệm không tồn tại.")

def calculate_interest():
    account_id = input("Nhập mã sổ tiết kiệm cần tính lãi: ").strip()
    for acc in saving_accounts:
        if acc["account_id"] == account_id:
            months = int(input("Nhập số tháng gửi: "))
            interest = acc["balance"] * acc["interest_rate"] * months / 12
            print(f"Tiền lãi sau {months} tháng: {interest:,.0f}đ")
            return
    print("Mã sổ tiết kiệm không tồn tại.")

def main():
    while True:
        print("\n=== SAVINGS ACCOUNT MANAGEMENT SYSTEM ===")
        print("1. Xem danh sách sổ tiết kiệm")
        print("2. Mở sổ tiết kiệm mới")
        print("3. Cập nhật sổ tiết kiệm")
        print("4. Tất toán sổ tiết kiệm")
        print("5. Tính tiền lãi")
        print("6. Thoát chương trình")
        choice = input("👉 Mời bạn chọn chức năng (1-6): ").strip()

        if choice == "1":
            view_accounts()
        elif choice == "2":
            open_account()
        elif choice == "3":
            update_account()
        elif choice == "4":
            close_account()
        elif choice == "5":
            calculate_interest()
        elif choice == "6":
            print("Cảm ơn bạn đã sử dụng hệ thống. Tạm biệt!")
            break
        else:
            print("Vui lòng nhập số từ 1-6.")

if __name__ == "__main__":
    main()
