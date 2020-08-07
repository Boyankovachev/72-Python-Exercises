# Write a program that accepts a sentence and calculate the number of letters and digits.
# Suppose the following input is supplied to the program: hello world!
# 123 Then,the output should be: LETTERS 10 DIGITS 3

print("Input a sentece: ", end="")
user_input = input()
count_digits = 0
count_letters = 0
for item in user_input:
    if(item>='0' and item<='9'):
        count_digits = count_digits + 1
    if(item>='a' and item<='z' or item>='A' and item<='Z'):
        count_letters = count_letters + 1
print("Count letters: ", str(count_letters))
print("Count digits: ", str(count_digits))