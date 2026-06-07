parking = []
next_id = 1

while True:
    print("==============================================================")
    print("             Quản Lý Bãi Xe - SMART PAKKING                     ")
    print("==============================================================")
    print("""
          1. thêm xe mới vào bãi
          2. hiển thị danh sách xe trong bãi
          3. xóa xe khỏi bãi (khi xe ra)
          4. thoát chương trình
          """)
    choice = input("Chọn (1-4): ")
    if choice == "4":
        print("thoát")
        break

    if choice == "1":
        brand=str(input("loại xe: "))
        name=str(input("chủ xe: "))
        
        if brand and name:
            parking.append({"id": next_id, "type": brand, "owner": name})
            print("Đã thêm xe ID", next_id)
            next_id += 1
        else: print("Không được để trống!")
        
    
    if choice == "2":
        if parking == []:
            print("bãi xe đang trống")
        
        else:
            print(f"{next_id: <3} | {brand: <20} | {name: <22} ")
            for i in parking:
                print(i)
    
    elif choice == "3":
        remove = input("Nhập ID xe cần xóa: ")
        if remove.isdigit():
            remove_id = int(remove)
            found = False
            for i in parking:
                if i["id"] == remove_id:
                    parking.remove(i)
                    print(f"Đã xóa xe ID {remove}")
                    found = True
                    break
            if not found:
                print("ID không tồn tại trong bãi xe")
        else:
            print("Vui lòng nhập số ID hợp lệ")

            
      

