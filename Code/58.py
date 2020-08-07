# Please write a program to generate all sentences where subject
# is in ["I", "You"] and verb is in ["Play", "Love"] and the object is in ["Hockey","Football"].

tuple1 = ("I", "You")
tuple2 = ("Play", "Love")
tuple3 = ("Hockey", "Football")
new_list = []
for tup1 in range(0, 2):
    for tup2 in range(0, 2):
        for tup3 in range(0, 2):
            flag = tuple1[tup1] + " " + tuple2[tup2] + " " + tuple3[tup3]
            new_list.append(flag)

print(new_list)
