# input nhap doanh thu cua tung ngay, revenue, total_revenue
# output tong doanh thu cua ca tuan, doanh thu tbinh, so ngay co doanh thu >= 5000000

revenue_everyday = 0
total_revenue = 0
target_revenue = 0

for i in range(1,8):
    revenue_everyday = int(input(f"Nhap doanh thu ngay {i}: "))
    total_revenue += revenue_everyday
    if revenue_everyday >= 5000000:
        target_revenue += 1

ave_revenue = total_revenue / 7

print("Tong doanh thu cua ca tuan: ", total_revenue)
print("Doanh thu tbinh moi ngay: ", ave_revenue)
print("So ngay dat duoc doanh thu (>= 5000000VND): ", target_revenue)
