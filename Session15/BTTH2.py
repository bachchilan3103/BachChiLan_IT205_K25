atm_vault_balance = 50000000  
user_account_balance = 10000000 
def display_balances():
    """
    Display current balances for debugging.
    Prints both user account balance and ATM vault balance.
    """
    global atm_vault_balance, user_account_balance
    print("--- SỐ DƯ TÀI KHOẢN ---")
    print(f"Tài khoản của bạn: {user_account_balance:,} VND")
    print(f"(Debug) Tiền mặt trong ATM: {atm_vault_balance:,} VND")


def deposit_money(amount):
    """
    Deposit money into user account and ATM vault.
    Parameters:
        amount (int): The amount of money to deposit.
    Returns:
        bool: True if deposit successful, False otherwise.
    """
    global atm_vault_balance, user_account_balance
    if amount <= 0:
        print("Số tiền không hợp lệ.")
        return False
    user_account_balance += amount
    atm_vault_balance += amount
    print(f"Giao dịch thành công! Số dư tài khoản hiện tại: {user_account_balance:,} VND.")
    return True


def check_withdrawal_rules(amount):
    """
    Check withdrawal rules before executing transaction.
    Parameters:
        amount (int): The amount of money user wants to withdraw.
    Returns:
        str: "INSUFFICIENT_FUNDS", "ATM_OUT_OF_CASH", "INVALID_AMOUNT", or "OK".
    """
    global atm_vault_balance, user_account_balance
    fee = 1100
    total_deduction = amount + fee

    if amount <= 0:
        return "INVALID_AMOUNT"
    if amount % 50000 != 0:
        return "INVALID_MULTIPLE"
    if total_deduction > user_account_balance:
        return "INSUFFICIENT_FUNDS"
    if amount > atm_vault_balance:
        return "ATM_OUT_OF_CASH"
    return "OK"


def execute_withdrawal(total_deduction, amount_to_dispense):
    """
    Execute withdrawal transaction.
    Parameters:
        total_deduction (int): Total amount deducted from user account (including fee).
        amount_to_dispense (int): Amount of cash dispensed to user.
    Returns:
        None
    """
    global atm_vault_balance, user_account_balance
    user_account_balance -= total_deduction
    atm_vault_balance -= amount_to_dispense
    print("Giao dịch đang xử lý...")
    print("Phí giao dịch: 1,100 VND")
    print(f"Bạn đã rút thành công {amount_to_dispense:,} VND.")
    print(f"Số dư tài khoản còn lại: {user_account_balance:,} VND.")


def main():
    """
    Main loop for SMART ATM system.
    Provides CLI interface for user to interact with ATM.
    """
    while True:
        print("\n============= SMART ATM =============")
        print("1. Xem số dư")
        print("2. Nạp tiền")
        print("3. Rút tiền")
        print("4. Kết thúc giao dịch")
        print("=====================================")
        choice = input("Vui lòng chọn giao dịch (1-4): ")

        if choice == "1":
            display_balances()

        elif choice == "2":
            print("--- NẠP TIỀN ---")
            try:
                amount = int(input("Nhập số tiền muốn nạp: "))
                deposit_money(amount)
            except ValueError:
                print("Dữ liệu nhập không hợp lệ.")

        elif choice == "3":
            print("--- RÚT TIỀN ---")
            try:
                amount = int(input("Nhập số tiền cần rút: "))
                status = check_withdrawal_rules(amount)
                if status == "INVALID_AMOUNT":
                    print("Số tiền không hợp lệ.")
                elif status == "INVALID_MULTIPLE":
                    print("Số tiền rút phải là bội số của 50,000.")
                elif status == "INSUFFICIENT_FUNDS":
                    print("Giao dịch thất bại: Số dư tài khoản không đủ.")
                elif status == "ATM_OUT_OF_CASH":
                    print("Giao dịch thất bại: Máy ATM không đủ tiền mặt để phục vụ.")
                elif status == "OK":
                    fee = 1100
                    total_deduction = amount + fee
                    execute_withdrawal(total_deduction, amount)
            except ValueError:
                print("Dữ liệu nhập không hợp lệ.")

        elif choice == "4":
            print("Cảm ơn quý khách đã sử dụng dịch vụ!")
            break

        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")

if __name__ == "__main__":
    main()
