"""
this is the bitwise swapping of
numbers using pthon programming
and bitwise operators , actually
we are going to use xor bitwis eoperator to solve this"""
print("numbers before swapping")
num1=int(input("num1="))
num2=int(input("num2="))
c=num1^num2
num1=c^num1
num2=c^num1
print("numbers after swapping")
print("num1=",num1)
print("num2=",num2)

