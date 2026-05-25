print("=== KIOSK PHÂN LUỒNG TỰ PHỤC VỤ - SỨC KHỎE VÀNG ===")

patient_name = input("Nhập họ và tên bệnh nhân (Ví dụ: Nguyen Van A): ").strip()
patient_age = int(input("Nhập tuổi bệnh nhân (Ví dụ: 25): "))
spo2_level = int(input("Nhập nồng độ oxy trong máu SpO2 từ 0-100 (Ví dụ: 96): "))
heart_rate = int(input("Nhập nhịp tim - nhịp/phút (Ví dụ: 80): "))
has_insurance = input("Bạn có thẻ BHYT không? (Vui lòng chỉ gõ 'yes' hoặc 'no'): ").strip().lower()

if spo2_level < 90 or heart_rate > 120:
    triage_status = "ĐỎ — Cấp cứu khẩn (Yêu cầu hỗ trợ y tế ngay lập tức!)"
elif (90 <= spo2_level <= 95) or (100 <= heart_rate <= 120):
    triage_status = "VÀNG — Theo dõi sát (Cần nhân viên y tế kiểm tra sớm)"
else:
    triage_status = "XANH — Khám thường (Vui lòng đợi theo STT tại sảnh)"

BASE_FEE = 500000

if patient_age < 6 or patient_age >= 80:
    advance_fee = 0
elif has_insurance == "yes":
    advance_fee = int(BASE_FEE * 0.5)
else:
    advance_fee = BASE_FEE

print("\n" + "="*55)
print("             PHIẾU KHÁM BỆNH ĐIỆN TỬ")
print("="*55)
print(f" Họ và tên bệnh nhân : {patient_name.upper()}")
print(f" Tuổi                : {patient_age}")
print(f" Chỉ số sinh hiệu    : SpO2 {spo2_level}% | Nhịp tim {heart_rate} bpm")
print(f" Thẻ Bảo hiểm Y tế   : {'Có' if has_insurance == 'yes' else 'Không'}")
print("-"*55)
print(f" MỨC ĐỘ PHÂN LUỒNG   : {triage_status}")
print(f" SỐ TIỀN TẠM ỨNG     : {advance_fee:,} VNĐ")
print("="*55)
print("  *Vui lòng cầm phiếu này đến quầy tiếp đón tương ứng.*")

print("\n" + "[LOG HỆ THỐNG - GIÁM SÁT KIỂU DỮ LIỆU KIOSK]")
print(f" Biến 'patient_name'  : Giá trị = '{patient_name}' | Kiểu dữ liệu = {type(patient_name)}")
print(f" Biến 'patient_age'   : Giá trị = {patient_age} | Kiểu dữ liệu = {type(patient_age)}")
print(f" Biến 'spo2_level'    : Giá trị = {spo2_level} | Kiêu dữ liệu = {type(spo2_level)}")
print(f" Biến 'heart_rate'    : Giá trị = {heart_rate} | Kiểu dữ liệu = {type(heart_rate)}")
print(f" Biến 'has_insurance' : Giá trị = '{has_insurance}' | Kiểu dữ liệu = {type(has_insurance)}")
print(f" Biến 'advance_fee'   : Giá trị = {advance_fee} | Kiểu dữ liệu = {type(advance_fee)}")
print("="*55)
