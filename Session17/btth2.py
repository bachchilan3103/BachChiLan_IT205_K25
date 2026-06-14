product_list = [
    "P01-Tai Nghe Bluetooth-550000-4.5",
    "P02-Chuột Không Dây-250000-4.8",
    "P03-Bàn Phím Cơ-850000-4.5"
]

def display_labels():
    print("--- DANH SÁCH TEM NHÃN ---")

    template = "Mã: {code} | Tên: {name} | Giá: {price} | Rating: {rating}"

    for product in product_list:
        try:
            info = product.split("-")

            data = {
                "code": f"{info[0]:<10}",
                "name": f"{info[1]:<20}",
                "price": f"{int(info[2]):,} VND",
                "rating": f"{info[3]}*"
            }

            print(template.format_map(data))

        except IndexError:
            print(f"Bỏ qua sản phẩm {info[0]} do sai cấu trúc dữ liệu")

        except ValueError:
            print(f"Bỏ qua sản phẩm {info[0]} do dữ liệu không hợp lệ")

def sort_products():
    print("--- SẮP XẾP SẢN PHẨM ---")

    valid_products = []

    for product in product_list:
        try:
            info = product.split("-")

            if len(info) < 4:
                raise IndexError

            price = info[2]
            rating = info[3]

            if not price.isdigit():
                raise ValueError

            valid_products.append(product)

        except IndexError:
            print(f"Bỏ qua sản phẩm {info[0]} do sai cấu trúc dữ liệu")

        except ValueError:
            print(f"Bỏ qua sản phẩm {info[0]} do dữ liệu không hợp lệ")

    valid_products.sort(
        key=lambda product: (
            -float(product.split("-")[3]),
            int(product.split("-")[2])
        )
    )

    for i in range(len(valid_products)):
        print(f"{i + 1}. {valid_products[i]}")

def calculate_total():
    print("--- TỔNG GIÁ TRỊ KHO ---")

    prices = []

    for product in product_list:
        try:
            info = product.split("-")

            if len(info) < 4:
                raise IndexError

            if not info[2].isdigit():
                raise ValueError

            prices.append(int(info[2]))

        except IndexError:
            print(f"Bỏ qua sản phẩm {info[0]} do sai cấu trúc dữ liệu")

        except ValueError:
            print(f"Bỏ qua sản phẩm {info[0]} do dữ liệu không hợp lệ")

    total = 0

    for price in prices:
        total += price

    print(f"Tổng giá trị các mặt hàng hiện tại là: {total:,} VND.")

while True:
    choice = input("""
============= E-COMMERCE ANALYTICS =============
1. Hiển thị tem nhãn sản phẩm (format_map & F-String)
2. Sắp xếp sản phẩm thông minh (sort key)
3. Tính tổng giá trị kho hàng
4. Đóng hệ thống
================================================
Chọn chức năng (1-4): """)

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ!")
        continue

    choice = int(choice)

    match choice:
        case 1:
            display_labels()

        case 2:
            sort_products()

        case 3:
            calculate_total()

        case 4:
            print("Đóng hệ thống!")
            break

        case _:
            print("Lựa chọn không hợp lệ!")