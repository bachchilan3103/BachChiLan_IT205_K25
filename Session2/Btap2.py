print("--- BLOOD DONOR SCREENING SYSTEM ---")
donor_age = int(input("Enter donor's age: "))
donor_weight = float(input("Enter donor's weight (kg): "))

if donor_age >= 18 and donor_weight >= 50:
    print("Result: ELIGIBLE. Please proceed to the blood donation room.")
else:
    print("Result: NOT ELIGIBLE. Thank you for your interest.")
    
    if donor_age < 18 and donor_weight < 50:
        print("Reason: You do not meet either the age (under 18) or weight (under 50kg) requirements.")
    elif donor_age < 18:
        print("Reason: You are under the required age limit (must be 18 or older).")
    else:
        print("Reason: You do not meet the minimum weight requirement (must be 50kg or heavier).")
