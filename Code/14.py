# Write a program that accepts a sentence and calculate the number of upper case
# letters and lower case letters. Suppose the following input is supplied to the program:
# Hello world! Then, the output should be: UPPER CASE 1 LOWER CASE 9

print("Input a sentece: ", end="")
user_input = input()
count_uppercase = 0
count_lowercase = 0
for item in user_input:
    if(item>='A' and item<='Z'):
        count_uppercase = count_uppercase + 1
    if(item>='a' and item<='z'):
        count_lowercase = count_lowercase + 1
print("Count_uppercase: ", str(count_uppercase))
print("Count_lowercase: ", str(count_lowercase))