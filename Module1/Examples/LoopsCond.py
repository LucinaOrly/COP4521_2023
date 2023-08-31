#While Loops

i = 1
while i < 4:
    print(i)
    i = i + 1
flag = True
while flag and i < 8:
    print(flag, i)
    i = i + 1


#if

a = 1
b = 0
if a:
    print("a is true!")
if not b:
    print("b is false!")
if a and b:
    print("a and b are true!")
if a or b:
    print("either a or b is true (or both are true)!")


#IFâ€¦elIfâ€¦.Else

a = 1
b = 0
c = 2
if a > b:
    if a > c:
        print("a is greatest")
    else:
        print("c is greatest")
elif b > c:
    print("b is greatest")
else:
    print("c is greatest")


#for loop

for i in range(0, 4):
    print(i)
for i in range(0,8,2):
    print(i)
for i in range(20,14,-2):
    print(i)


#manipulating loop structures

for num in range(10,20):
    if num%2 == 0:
        continue
    prime=True
    for i in range(3,num):
        if num%i == 0:
            prime=False
            break
    if (prime):
        print(num, 'is a prime number')


# Sum of Even Terms in Fibonacci sequence

total = 0
f1, f2 = 1, 2
while f1 < 4000000:
    if f1 % 2==0:
        total=total + f1
    f1, f2 = f2,f1+ f2
print(total)
