import re
from tkinter import *

window = Tk()
window.geometry("480x300")
window.title("Password Strength Checker")
window.config(bg="#00574a")

title = Label(window, text="Password Strength Checker", font=("fixedsys", 18, "bold"), fg="#ffffff", bg="#00574a")
title.pack(pady=10)

image = PhotoImage(file='lockpix.png')
shrink = image.subsample(5, 5)

picture = Label(window, image=shrink)
picture.pack(padx=10, pady=10)

enter = Entry(window, justify="center", show="*", width=30, fg="#00574a", bg="#ffffff")
enter.pack(pady=10)

result = Label(window, text="", font=("Times New Roman", 14), bg="#00574a", fg="#ffffff")
result.pack(pady=20)


def check_password():
    password = enter.get()
    score = 0

    if len(password) >= 8:
        score += 1

    if re.search(r"[A-Z]", password):
        score += 1

    if re.search(r"[a-z]", password):
        score += 1

    if re.search(r"[0-9]", password):
        score += 1

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    if score == 5:
        strength = "Very Strong"
    elif score == 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"
    elif score == 2:
        strength = "Weak"
    else:
        strength = "Very Weak"

    result.config(text=f"Strength: {strength}")


Button(window, text="Check Password", command=check_password, fg="#fc5c5c", bg="#fbe8e6", font=("fixedsys", 12)).pack(pady=10)



window.mainloop()
