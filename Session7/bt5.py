# ==============================
# HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO
# ==============================

raw_batch = " LAP-VN-23-001 ; mou-us-24-012 ; KEY-vn-23-abc ; lap-JP-22-045 ; MOn-vn-24-099 "

while True:
    print("\n===== HỆ THỐNG GIẢI MÃ DỮ LIỆU KHO HÀNG =====")
    print("1. Hiển thị chuỗi mã vạch gốc")
    print("2. Giải mã, làm sạch và in báo cáo kiểm kê")
    print("3. Tra cứu nhanh theo đuôi Serial")
    print("4. Thoát chương trình")

    choice = input("Nhập lựa chọn của bạn (1-4): ").strip()

    if choice == "1":
        print("\nChuỗi mã vạch gốc:")
        print(raw_batch)

    elif choice == "2":
        product_list = raw_batch.split(";")

        print("\n===== BÁO CÁO KIỂM KÊ =====")
        print(f"{'MÃ SP':<10}{'XUẤT XỨ':<12}{'NĂM SX':<10}{'SERIAL':<10}{'TRẠNG THÁI'}")

        total_product = 0
        valid_product = 0

        for item in product_list:
            code = item.strip().upper()

            parts = code.split("-")

            if len(parts) == 4:
                product_type = parts[0]
                country = parts[1]
                year = "20" + parts[2]
                serial = parts[3]

                total_product += 1

                if serial.isdigit():
                    status = "Pass"
                    valid_product += 1
                else:
                    status = "Lỗi Serial - Reject"

                print(
                    f"{product_type:<10}"
                    f"{country:<12}"
                    f"{year:<10}"
                    f"{serial:<10}"
                    f"{status}"
                )

        print(f"\nĐã giải mã thành công {valid_product} sản phẩm hợp lệ / Tổng số {total_product} sản phẩm.")

    elif choice == "3":
        search_serial = input("Nhập 2 số cuối của Serial cần tìm: ").strip()

        product_list = raw_batch.split(";")

        found = False

        for item in product_list:
            code = item.strip().upper()

            parts = code.split("-")

            if len(parts) == 4:
                serial = parts[3]

                if serial[-2:] == search_serial:
                    print("\nTìm thấy sản phẩm:")
                    print(code)
                    found = True

        if found == False:
            print("\nKhông tìm thấy sản phẩm phù hợp.")

    elif choice == "4":
        print("\nĐóng ca kiểm kho. Chào tạm biệt!")
        break

    else:
        print("\nChức năng không tồn tại, vui lòng nhập số từ 1-4!")
