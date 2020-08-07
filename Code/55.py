# Please write a program to compress and decompress the string "hello world!hello world!hello world!hello world!".


import zlib

string = b"hello world!hello world!hello world!hello world!"
string = zlib.compress(string)
print(zlib.decompress(string))
