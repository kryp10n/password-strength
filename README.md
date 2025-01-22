# Password Strength Checker
A Python-based password strength checker with a simple GUI built using `ttkbootstrap`. The tool checks the strength of passwords, generates secure passwords, and checks if they have been compromised using the Have I Been Pwned API.

## Features
- Password Strength Checker: Checks if a password meets the necessary strength requirements (minimum length, contains digits, uppercase, lowercase, and the '@' symbol).
- Password Generator: Generates a secure password that includes at least one lowercase letter, one uppercase letter, one digit, and the '@' symbol.
- Compromised Password Check: Verifies if a password has been leaked in known data breaches using the Have I Been Pwned API.
- Modern UI: The app uses the `ttkbootstrap` library to create a clean, modern interface.

## Installation
1. Clone the repository: git clone https://github.com/yourusername/password-strength-checker.git
2. Install the required dependencies: pip install ttkbootstrap requests


## Usage
1. Run the `ui.py` script: python ui.py
2. The application will open a window where you can:
   - Enter a password to check its strength.
   - Generate a new secure password.
   - Check if the password has been compromised.

## Requirements
- Python 3.x
- `ttkbootstrap` for the modern UI.
- `requests` to interact with the Have I Been Pwned API.

## License
This project is for educational purposes only. Feel free to modify and use the code for personal or educational use.