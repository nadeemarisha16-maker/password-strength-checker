# password-strength-checker
A GUI-based password strength checker built with Python and Tkinter, using regex to score passwords against common security criteria.
# Password Strength Checker

A simple desktop GUI application that evaluates password strength in real time. 
Built with Python's Tkinter for the interface and regular expressions to check 
for common password complexity requirements.

## Features
- Clean, styled GUI built with Tkinter
- Checks passwords against 5 strength criteria:
  - Minimum length (8+ characters)
  - Contains uppercase letters
  - Contains lowercase letters
  - Contains numbers
  - Contains special characters
- Displays a strength rating: Very Weak, Weak, Medium, Strong, or Very Strong
- Password input is masked for privacy

## How It Works
The app uses Python's `re` module to run pattern checks against the entered 
password. Each satisfied criterion adds a point to a running score, which is 
then mapped to a strength label and displayed to the user.

## Tech Stack
- Python 3
- Tkinter (GUI)
- `re` (regex pattern matching)

## Run It
```bash
python password_strength_checker.py
```

## Possible Future Improvements
- Add a check against common/breached password lists (e.g., via the 
  Have I Been Pwned API)
- Add a visual strength meter (progress bar or color-coded indicator)
- Provide specific feedback on which criteria are missing, not just a score
