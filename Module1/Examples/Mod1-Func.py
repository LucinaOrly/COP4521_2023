#example 1
"""
def	connect(uname,	pword,	server,	port):
    print("Connecting	to",	server,	":",	port,	"...")
    #	Connecting	code	here	...

#example of calls
connect('admin',	'ilovecats',	'shell.cs.fsu.edu',	9160)
connect('jdoe',	'r5f0g87g5@y',	'linprog.cs.fsu.edu',	6370)
"""

#example 2
#import adder
"""

def	connect(uname,	pword,	server=	'localhost',	port	=	9160):
    print("Connecting	to",	server,	":",	port,	"...")
    #	Connecting	code	here	...

connect('admin',	'ilovecats')
connect('admin',	'ilovecats',	'shell.cs.fsu.edu')
connect('admin',	'ilovecats',	'shell.cs.fsu.edu',	6379)
"""

"""
from adder import *
X=add_item(3)
X=add_item(4,X)
X=add_item(5,X)
"""

"""
def	connect(uname,	pword,	server	=	'localhost',	port	=	9160):
    print("Connecting	to",	server,	":",	port,	"...")
    #	Connecting	code	here	...

connect('admin',	'ilovecats',	'shell.cs.fsu.edu',	6379)


#valid test

connect('admin',	'ilovecats',	'shell.cs.fsu.edu')

connect(uname='admin',	pword='ilovecats',	'shell.cs.fsu.edu')

connect('admin',	'ilovecats',	port=6379,	server='shell.cs.fsu.edu')
"""

#Packing example
"""
def	example(param1,	*args,	**kwargs):
    print	("param1:",	param1)
    for	arg	in	args:
        print	(arg)
    for	key	in	kwargs.keys():
        print	(key,	":",	kwargs[key])

example('one',	'two',	'three',	server='localhost',	port=9160)
"""

#example2
"""
def	func(arg1,	arg2,	arg3):
    print(arg1)
    print(arg2)
    print(arg3)



args = ("one", 2, 3)
func(*args)



kwargs	=	{"arg3":	3,	"arg1":	"one",	"arg2":	2}
func(**kwargs)
"""


def	f(x):
    return	x**2

print(f(8))
g =	lambda	x:	x**2
print(g(8))
