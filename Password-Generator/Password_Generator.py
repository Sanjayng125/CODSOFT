import random

pass_len = 5
def getLen():
    global pass_len
    pass_len = int(input("Enter password length:"))
getLen()
if pass_len < 5:
    print("For secure password minimum length should be 5!!")
    getLen()
elif pass_len > 20:
    print("Maximum length is 20")
    pass_len = 20

all_chars = ["!@#$%^&*~", "abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ", "0123456789"]
password = ""
for i in range(0, pass_len):
    temp1 = random.randint(0, len(all_chars)-1)
    temp2 = all_chars[temp1]
    temp3 = random.randint(0, len(temp2)-1)
    password += temp2[temp3]
spec_contains = False
for i in range(0, len(all_chars[0])):
    if all_chars[0][i] in password:
        spec_contains = True
if len(password) < 6 and not spec_contains:
    print(f"{password} - Weak")
elif len(password) <= 6 and spec_contains:
    print(f"{password} - Medium")
elif len(password) < 9 and not spec_contains:
    print(f"{password} - Medium")
elif len(password) <= 9 and spec_contains:
    print(f"{password} - Strong")
elif len(password) < 13 and not spec_contains:
    print(f"{password} - Strong")
elif len(password) < 13 and spec_contains:
    print(f"{password} - Very Strong")
elif len(password) < 19:
    print(f"{password} - Very Strong")

