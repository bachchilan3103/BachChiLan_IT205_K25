raw_logs = []
processed_logs = []

def clean_logs():
    """
    Nhập và làm sạch dữ liệu log thô.
    """
    print("--- NẠP DỮ LIỆU LOG ---")

    logs = input("Nhập chuỗi log thô (cách nhau bởi dấu ;): ")

    table = str.maketrans("", "", "!@#$")

    cleaned_logs = logs.translate(table)

    raw_logs = [log.strip() for log in cleaned_logs.split(";")]

    print(f"Đã làm sạch và lưu {len(raw_logs)} dòng log vào hệ thống.")

    return raw_logs

def filter_logs(raw_logs):
    """
    Lọc các log chứa ERROR hoặc CRITICAL.
    """
    if len(raw_logs) == 0:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
        return []

    print("--- LỌC CẢNH BÁO ---")

    processed_logs = [
        log for log in raw_logs
        if "ERROR" in log.upper() or "CRITICAL" in log.upper()
    ]

    print(f"Tìm thấy {len(processed_logs)} cảnh báo nguy hiểm:")

    for log in processed_logs:
        print(f"- {log}")

    return processed_logs

def mask_ip(log):
    """
    Mã hóa địa chỉ IP trong một dòng log.
    """
    words = log.split()

    for i in range(len(words)):
        if "." in words[i]:
            ip_parts = words[i].split(".")

            if len(ip_parts) == 4:
                ip_parts[2] = "*"
                ip_parts[3] = "*"
                words[i] = ".".join(ip_parts)

    return " ".join(words)

def generate_safe_report(processed_logs):
    """
    Tạo báo cáo log đã mã hóa IP.
    """
    if len(processed_logs) == 0:
        print("Chưa có dữ liệu log, vui lòng thực hiện chức năng 1")
        return []

    print("--- MÃ HÓA IP ---")

    safe_logs = []

    for log in processed_logs:
        safe_logs.append(mask_ip(log))

    print("Báo cáo log an toàn:")

    for index, log in enumerate(safe_logs, start=1):
        print(f"{index}. {log}")

    return safe_logs

while True:
    choice = input("""
============= SECURITY LOG ANALYZER =============
1. Nhập và làm sạch dữ liệu Log thô
2. Lọc các Log cảnh báo mức độ cao (ERROR/CRITICAL)
3. Mã hóa địa chỉ IP (Masking)
4. Đóng hệ thống
=================================================
Chọn chức năng (1-4): """)

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ!")
        continue

    choice = int(choice)

    match choice:
        case 1:
            raw_logs = clean_logs()

        case 2:
            processed_logs = filter_logs(raw_logs)

        case 3:
            generate_safe_report(processed_logs)

        case 4:
            print("Đóng hệ thống!")
            break

        case _:
            print("Lựa chọn không hợp lệ!")