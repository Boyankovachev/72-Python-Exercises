# Please write assert statements to verify that every number in the list [2,4,6,8] is even.

print("Please inut list of numers:", end="")
user_input = input()
list_input = user_input.split(",")
for item in list_input:
    assert int(item) % 2 == 0
