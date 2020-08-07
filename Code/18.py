# A website requires the users to input username and password to register.
# Write a program to check the validity of password input by users.
# Following are the criteria for checking the password:
#  1. At least 1 letter between [a-z]
#  2. At least 1 number between [0-9]
#  3. At least 1 letter between [A-Z]
#  4. At least 1 character from [$#@]
#  5. Minimum length of transaction password: 6
#  6. Maximum length of transaction password: 12
# Your program should accept a sequence of comma separated passwords and will
# check them according to the above criteria. Passwords that match the criteria
# are to be printed, each separated by a comma. Example If the following
# passwords are given as input to the program: ABd1234@1,a F1#,2w3E*,2We3345 Then,
# the output of the program should be: ABd1234@1

def password_check(input_password):
    if len(input_password) > 12:
        return False

    if len(input_password) < 6:
        return False

    flag = False
    for item in input_password:
        if 'a' <= item <= 'z':
            flag = True
            break
    if not flag:
        return False

    flag = False
    for item in input_password:
        if 'A' <= item <= 'Z':
            flag = True
            break
    if not flag:
        return False

    flag = False
    for item in input_password:
        if '0' <= item <= '9':
            flag = True
            break
    if not flag:
        return False

    flag = False
    for item in input_password:
        if item == '$' or item == '#' or item == '@':
            flag = True
    if not flag:
        return False

    return True


print("Enter a sequence of comma separated passwords")
user_input = input()
input_list = user_input.split(",")
correct_passwords = []
for password in input_list:
    if password_check(password):
        correct_passwords.append(password)

print(correct_passwords)
