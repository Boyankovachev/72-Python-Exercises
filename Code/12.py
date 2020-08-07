# Write a program, which will find all such numbers between 1000 and 3000 (both included)
# such that each digit of the number is an even number. The numbers obtained should be
# printed in a comma-separated sequence on a single line.

def are_all_numbers_even(num):
    str_num = str(num)
    for number in str_num:
        if int(number) % 2 != 0:
            return False
    return True


winner_numbers = []
for x in range(1000, 3001):
    if (are_all_numbers_even(x)):
        winner_numbers.append(x)
print(winner_numbers)
