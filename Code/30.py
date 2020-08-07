# Define a function that can accept two strings as input and print the string with maximum length in console.
# If two strings have the same length, then the function should print al l strings line by line.


def longer_str(str1, str2):
    if len(str1) == len(str2):
        return [str1, str2]
    elif len(str1) > len(str2):
        return str1
    elif len(str1) < len(str2):
        return str2


print(longer_str("qwerty", "asdf"))
