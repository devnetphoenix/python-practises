array = []
sequence = []
n = int(input("enter nmber of element in array = "))
for i in range(n):
    p=int(input("element ="))
    array.append(p)
print(array)

n2 = int(input("enter number of element in seq = "))
for i in range(n2):
    q=int(input("element = "))
    sequence.append(q)
print(sequence)

'''if len(array)<len(check):
    print(false)

check = []

for i in sequence:
    for j in array:
        if i==j:
            check.append(array.index(j))
        pass
print(check)
if sorted(check) == check:
    print("yes")
else:
    print("no")'''
n1 = len(array)
n2 = len(sequence)
if n1<n2:
    print("false")
	
for i in array:
    for j in sequence:
        if i != j:
            array.remove(i)
        else:
            array.remove(i)
            sequence.remove(j)
print(array)
print(sequence)

	
	




        
