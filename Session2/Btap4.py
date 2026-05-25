print("--- HỆ THỐNG SÀNG LỌC TIỀN PHẪU THUẬT ---")

age = int(input("Nhập tuổi bệnh nhân: "))
systolic_bp = int(input("Nhập huyết áp tâm thu (mmHg): "))
blood_sugar = int(input("Nhập lượng đường huyết (mg/dL): "))

if age < 0 or systolic_bp < 0 or blood_sugar < 0:
    print("Dữ liệu nhập vào không hợp lệ (Không được nhập số âm)!")

elif age >= 75:
    print("Kết luận: TỪ CHỐI PHẪU THUẬT.")
    print("Lý do: Bệnh nhân vượt quá độ tuổi phẫu thuật an toàn (phải dưới 75 tuổi).")

elif systolic_bp < 90 or systolic_bp > 140:
    print("Kết luận: TỪ CHỐI PHẪU THUẬT.")
    print("Lý do: Huyết áp tâm thu nằm ngoài vùng an toàn (phải từ 90 đến 140 mmHg).")

elif blood_sugar >= 150:
    print("Kết luận: TỪ CHỐI PHẪU THUẬT.")
    print("Lý do: Đường huyết cao nguy hiểm (phải dưới 150 mg/dL).")

else:
    print("Kết luận: ĐỦ ĐIỀU KIỆN PHẪU THUẬT.")
