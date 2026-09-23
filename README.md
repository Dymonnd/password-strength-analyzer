# 🔐 Python Password Strength Analyser

A Python-based password strength analyser developed as part of my Cyber Security studies.

This project evaluates passwords based on length, character complexity and whether they appear in a list of commonly used passwords. It provides a strength rating and recommendations to help users understand what makes a password more secure.

## Features

* Analyses password length and character complexity.
* Detects uppercase and lowercase letters, numbers and symbols.
* Checks passwords against a common password wordlist.
* Calculates a password strength score.
* Categorises passwords as Weak, Moderate or Strong.
* Provides recommendations for improving password strength.

## How It Works

The program evaluates the password using several criteria:

| Criteria                   | Points |
| -------------------------- | -----: |
| Each character             |     +1 |
| Contains uppercase letters |     +2 |
| Contains lowercase letters |     +2 |
| Contains numbers           |     +2 |
| Contains symbols           |     +3 |

The final score determines the password strength rating.

Passwords found in the common password wordlist are automatically rated as Weak, regardless of their complexity score.

## Getting Started

**Requirements:**

* Python 3
* The included `common_passwords.txt` file

**Running the program:**

Clone the repository:

```bash
git clone https://github.com/Dymonnd/password-strength-analyzer.git
```

Navigate into the project folder:

```bash
cd password-strength-analyzer
```

Run the Python script:

```bash
python passwordstrength.py
```

Enter a password when prompted to view its analysis and suggestions.

Type `quit` to exit the program.

## What I Learned

Through this project, I developed my understanding of:

* Python functions, loops and conditional statements.
* File handling and exception handling.
* Working with strings and character validation.
* Password security principles and common password vulnerabilities.
* Using Python to develop basic cyber security tools.

## Future Improvements

* Detect repeated characters and predictable password patterns.
* Improve the scoring system to better reflect password security.
* Add a secure password generator.
* Develop a graphical user interface (GUI).

## Security Disclaimer

This project is intended for educational purposes and provides a basic password complexity assessment. A Strong rating does not guarantee that a password is secure.

Passwords are analysed locally, but input is visible in the terminal. Users should test the program with example passwords rather than their actual account credentials.
