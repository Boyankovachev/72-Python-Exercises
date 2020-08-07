#With a given int n, write a program to generate a dictionary that contains (i, i*i)

print('Input a number: ', end=" ")
n = int(input())
dic = {}
if(n>0):
    for i in range(1, n+1):
        dic[i] = i*i
if(n<0):
    for i in range(n, 0):
        dic[i] = i*i
print(dic)