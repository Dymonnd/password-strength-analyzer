
import tkinter as tk
from tkinter import ttk
from pathlib import Path
import secrets
import string


# Load common passwords
password_file = Path(__file__).with_name("common_passwords.txt")

if password_file.exists():
    with open(password_file, "r", encoding="utf-8", errors="ignore") as file:
        common_passwords = {
            line.strip().lower()
            for line in file
            if line.strip()
        }
else:
    common_passwords = set()


# Password analysis
def analyze_password():
    password = password_entry.get()

    if not password:
        result_label.config(text="Please enter a password.", fg="orange")
        return

    length = len(password)

    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_symbol = any(not c.isalnum() for c in password)

    is_common = password.lower() in common_passwords
    is_repeated = len(set(password)) == 1

    # Calculate score
    score = length

    if has_upper:
        score += 2
    if has_lower:
        score += 2
    if has_digit:
        score += 2
    if has_symbol:
        score += 3

    # Determine strength
    if is_common or is_repeated or length < 8 or score < 8:
        rating = "Weak"
        colour = "#ef4444"

    elif length < 12 or score < 12:
        rating = "Moderate"
        colour = "#f59e0b"

    else:
        rating = "Strong"
        colour = "#22c55e"

    # Update strength display
    result_label.config(
        text=f"{rating} | Score: {score}",
        fg=colour
    )

    strength_bar["value"] = min(score * 4, 100)

    # Generate suggestions
    suggestions = []

    if is_common:
        suggestions.append("Avoid commonly used passwords.")

    if is_repeated:
        suggestions.append("Avoid repeating the same character.")

    if length < 12:
        suggestions.append("Use at least 12 characters.")

    if not has_upper:
        suggestions.append("Add uppercase letters.")

    if not has_lower:
        suggestions.append("Add lowercase letters.")

    if not has_digit:
        suggestions.append("Add numbers.")

    if not has_symbol:
        suggestions.append("Add special characters.")

    if not password_file.exists():
        suggestions.append("Common password wordlist not found.")

    if not suggestions:
        suggestions.append("All basic complexity checks passed!")

    suggestions_label.config(
        text="\n".join("• " + item for item in suggestions)
    )


# Show / hide password
def toggle_password():
    if show_password.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")


# Generate a secure password
def generate_password():

    length = 18

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    numbers = string.digits
    symbols = "!@#$%^&*"

    all_characters = uppercase + lowercase + numbers + symbols

    # Ensure at least one character from each category
    password = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(numbers),
        secrets.choice(symbols)
    ]

    # Fill the remaining characters
    for _ in range(length - 4):
        password.append(secrets.choice(all_characters))

    # Shuffle the characters
    secrets.SystemRandom().shuffle(password)

    generated_password = "".join(password)

    # Display the generated password
    password_entry.delete(0, tk.END)
    password_entry.insert(0, generated_password)

    # Automatically analyse it
    analyze_password()

    copy_status_label.config(text="")


# Copy password to clipboard
def copy_password():

    password = password_entry.get()

    if not password:
        copy_status_label.config(
            text="Generate or enter a password first.",
            fg="#f59e0b"
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)

    copy_status_label.config(
        text="Password copied to clipboard!",
        fg="#22c55e"
    )

# Main application window
root = tk.Tk()

root.title("Password Strength Analyser")
root.geometry("520x680")
root.configure(bg="#111827")
root.resizable(False, False)


# Title
title = tk.Label(
    root,
    text="PASSWORD STRENGTH ANALYSER",
    font=("Arial", 16, "bold"),
    bg="#111827",
    fg="#22c55e"
)

title.pack(pady=25)


# Description
description = tk.Label(
    root,
    text="Analyse your password security",
    font=("Arial", 11),
    bg="#111827",
    fg="white"
)

description.pack(pady=5)


# Password input
password_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=32,
    show="*"
)

password_entry.pack(pady=20)


# Show password checkbox
show_password = tk.BooleanVar()

show_checkbox = tk.Checkbutton(
    root,
    text="Show password",
    variable=show_password,
    command=toggle_password,
    bg="#111827",
    fg="white",
    selectcolor="#374151",
    activebackground="#111827",
    activeforeground="white"
)

show_checkbox.pack()


# Password generator button
generate_button = tk.Button(
    root,
    text="GENERATE PASSWORD",
    command=generate_password,
    bg="#3b82f6",
    fg="white",
    font=("Arial", 11, "bold"),
    width=25,
    height=2
)

generate_button.pack(pady=10)


# Copy password button
copy_button = tk.Button(
    root,
    text="COPY PASSWORD",
    command=copy_password,
    bg="#374151",
    fg="white",
    font=("Arial", 11, "bold"),
    width=25,
    height=2
)

copy_button.pack(pady=5)


# Clipboard status message
copy_status_label = tk.Label(
    root,
    text="",
    font=("Arial", 10),
    bg="#111827",
    fg="#22c55e"
)

copy_status_label.pack(pady=5)

# Analyse button
analyse_button = tk.Button(
    root,
    text="ANALYSE PASSWORD",
    command=analyze_password,
    bg="#22c55e",
    fg="black",
    font=("Arial", 11, "bold"),
    width=25,
    height=2
)

analyse_button.pack(pady=20)


# Strength rating
result_label = tk.Label(
    root,
    text="Enter a password to begin",
    font=("Arial", 14, "bold"),
    bg="#111827",
    fg="white"
)

result_label.pack(pady=10)


# Strength progress bar
strength_bar = ttk.Progressbar(
    root,
    length=350,
    maximum=100
)

strength_bar.pack(pady=10)


# Suggestions
suggestions_label = tk.Label(
    root,
    text="",
    font=("Arial", 10),
    bg="#111827",
    fg="white",
    justify="left"
)

suggestions_label.pack(pady=20)


# Start application
root.mainloop()