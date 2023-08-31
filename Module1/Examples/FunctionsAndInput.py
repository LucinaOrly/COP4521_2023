
# Defining the function
"""
def print_greeting():
    print ("Hello!")
    print ("How are you today?")

# Calling the function
print_greeting()
"""

#parameters and return values
"""
def hello_func(name,somelist):
    print ("Hello,", name, "!\n")
    name = "Alice"
    somelist[0] = 3
    return 1, 2
myname = "Ben"
mylist = [1,2]
a,b = hello_func(myname, mylist)
print (myname, mylist)
print (a, b)
"""

#variables
"""
def hello_func(names):
    for n in names:
        print ("Hello,", n, "!")
    names[0] = 'Susie'
    names[1] = 'Pete'
    names[2] = 'Will'
names = ['Susan', 'Peter', 'William']
hello_func(names)
print ("The names are now", names, ".")
"""

# Sum of Even Terms in Fibonacci sequence
"""
def even_fib():
    total = 0
    f1, f2 = 1, 2
    while f1 < 4000000:
        if f1 % 2	== 0:
            total = total + f1
        f1, f2 = f2,f1	+ f2
    return total
if __name__ == "__main__":
    print(even_fib())
"""

# Sum of Even Terms in Fibonacci sequence
#with input
"""
def even_fib(limit):
    total = 0
    f1, f2 = 1, 2
    while f1 < limit:
        if f1 % 2	== 0:
            total = total + f1
        f1, f2 = f2,f1	+ f2
    return total

if	__name__ 	=="__main__":
    limit = input("Enter the max Fibonacci number: ")
    print(even_fib(int(limit)))
"""

#input
"""
name = input("Enter in your name...")
age = int(input("Enter in your age..."))
while ((age<0)or (age>108)):
    age = int(input("Enter in your age..."))
print(name)
print(age)
"""