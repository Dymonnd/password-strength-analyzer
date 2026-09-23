

def load_common_passwords(filename="common_passwords.txt"):
    try:
        with open(filename, "r", encoding="utf-8", errors="ignore") as file:
            return set(line.strip().lower() for line in file if line.strip())
    except FileNotFoundError:
        print(f"⚠ Could not find '{filename}'.")
        return set()


def password_strength_calculator():
    common_passwords = load_common_passwords()

    while True:
        password = input("\nEnter password to analyze (or type 'quit' to exit): ")

        if password.strip().lower() == "quit":
            print("Goodbye.")
            break

        is_common = password.strip().lower() in common_passwords

        
        length = len(password)

        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_symbol = any(not c.isalnum() for c in password)

       
        score = length
        if has_upper:
            score += 2
        if has_lower:
            score += 2
        if has_digit:
            score += 2
        if has_symbol:
            score += 3

        print("\n--- Password Analysis ---")
        print(f"Length: {length}")
        print(f"Has uppercase: {has_upper}")
        print(f"Has lowercase: {has_lower}")
        print(f"Has digit: {has_digit}")
        print(f"Has symbol: {has_symbol}")
        print(f"Score: {score}")

        # Rating (override if common)
        if is_common:
            rating = "Weak"
            print("Common password: YES (easy to guess)")
        else:
            print("Common password: NO (not found in list)")
            if score < 8:
                rating = "Weak"
            elif score < 12:
                rating = "Moderate"
            else:
                rating = "Strong"

        print(f"Rating: {rating}")

        
        print("\n--- Suggestions ---")
        if is_common:
            print("- Do NOT use common passwords (choose something unique).")
        if length < 12:
            print("- Make it longer (12+ characters recommended).")
        if not has_upper:
            print("- Add at least one uppercase letter (A-Z).")
        if not has_lower:
            print("- Add at least one lowercase letter (a-z).")
        if not has_digit:
            print("- Add at least one number (0-9).")
        if not has_symbol:
            print("- Add at least one symbol (!@#$ etc.).")

        if (not is_common) and length >= 12 and has_upper and has_lower and has_digit and has_symbol:
            print("- Looks great ✅")


password_strength_calculator()