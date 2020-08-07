# Assuming that we have some email addresses in the "username@companyname.com" format,
# please write program to print the user name of a given email address.
# Both user names and company names are composed of letters only.

print("Input a valid email adress")
while True:
    email = input()
    if email.count("@") >= 1:
        break
    else:
        print("This is invalid email adress")

print(email.split("@")[0])