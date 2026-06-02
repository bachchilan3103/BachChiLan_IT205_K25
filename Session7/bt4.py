raw_data = " eMP-001; nguyen van a ;0987654321;sale | Emp-002; Tran Thi B; 0912-345-678 ; mkt | EMP-003 ; le van C ; 0988abc123 ; IT "

while True:
    print("\n===== HỆ THỐNG QUẢN LÝ NHÂN SỰ =====")
    print("1. Hiển thị chuỗi dữ liệu gốc")
    print("2. Chuẩn hóa dữ liệu và in báo cáo")
    print("3. Tìm kiếm nhân viên theo mã ID")
    print("4. Thoát chương trình")

    choice = input("Chọn chức năng (1-4): ").strip()

    if choice == "1":
        print(raw_data)

    elif choice == "2":
        print(f"\n{'MÃ ID':<10} | {'HỌ VÀ TÊN':<20} | {'SỐ ĐIỆN THOẠI':<15} | {'PHÒNG BAN':<10}")
        print("-" * 65)

        for item in raw_data.split("|"):
            parts = item.split(";")
            emp_id = parts[0].strip().upper()
            name = parts[1].strip().title()
            phone = parts[2].strip().replace("-", "")
            dept = parts[3].strip().upper()

            if phone.isdigit():
                phone = "******" + phone[-4:]
            else:
                phone = "Invalid Format"

            print(f"{emp_id:<10} | {name:<20} | {phone:<15} | {dept:<10}")

    elif choice == "3":
        search_id = input("Nhập mã nhân viên cần tìm: ").strip().upper()
        found = False

        for item in raw_data.split("|"):
            parts = item.split(";")
            emp_id = parts[0].strip().upper()

            if emp_id == search_id:
                name = parts[1].strip().title()
                phone = parts[2].strip().replace("-", "")
                dept = parts[3].strip().upper()

                if phone.isdigit():
                    phone = "******" + phone[-4:]
                else:
                    phone = "Invalid Format"

                print(f"Mã NV: {emp_id} - Tên: {name} - SĐT: {phone} - Phòng: {dept}")
                found = True
                break

        if not found:
            print("Không tìm thấy nhân viên")

    elif choice == "4":
        print("Thoát chương trình")
        break

    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")
