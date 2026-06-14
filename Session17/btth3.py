teams_list = []
match_schedule = []

def input_teams():
    print("--- NHẬP DANH SÁCH ---")

    teams = input("Nhập các đội (cách nhau bởi dấu phẩy): ")

    teams_list = [team.strip().upper() for team in teams.split(",")]

    temp = []
    for team in teams_list:
        if team not in temp:
            temp.append(team)

    teams_list = temp

    print(f"Đã ghi nhận {len(teams_list)} đội: {teams_list}")

    return teams_list

def create_schedule(teams_list):
    if len(teams_list) < 2:
        print("Lỗi: Cần tối thiểu 2 đội để tạo lịch thi đấu.")
        return []

    print("--- LỊCH THI ĐẤU VÒNG BẢNG ---")

    match_schedule = []

    for i in range(len(teams_list)):
        for j in range(i + 1, len(teams_list)):
            match_schedule.append(f"{teams_list[i]} vs {teams_list[j]}")

    for i in range(len(match_schedule)):
        print(f"{i + 1}. {match_schedule[i]}")

    print(f"Tổng số trận đấu: {len(match_schedule)} trận.")

    return match_schedule

def create_match_id(match_schedule):
    if len(match_schedule) == 0:
        print("Vui lòng tạo lịch thi đấu trước khi sinh mã ID.")
        return

    print("--- MÃ TRẬN ĐẤU (MATCH ID) ---")

    for i in range(len(match_schedule)):
        match = match_schedule[i]

        team_1, team_2 = match.split(" vs ")

        code_1 = f"{team_1[:3]:X<3}"
        code_2 = f"{team_2[:3]:X<3}"

        match_id = f"M{i + 1:02d}-{code_1}-{code_2}"

        print(f"Trận {i + 1} ({match}) -> ID: {match_id}")

while True:
    choice = input("""
============= ESPORTS MATCHMAKER =============
1. Nhập danh sách Đội tuyển
2. Tạo lịch thi đấu (Combinations)
3. Tạo mã trận đấu tự động (F-String & Cắt chuỗi)
4. Đóng hệ thống
==============================================
Chọn chức năng (1-4): """)

    if not choice.isdigit():
        print("Lựa chọn không hợp lệ! Vui lòng nhập (1-4)")
        continue

    choice = int(choice)

    match choice:
        case 1:
            teams_list = input_teams()

        case 2:
            match_schedule = create_schedule(teams_list)

        case 3:
            create_match_id(match_schedule)

        case 4:
            print("Đóng hệ thống!")
            break

        case _:
            print("Lựa chọn không hợp lệ!")