#A simple example of creating a list of squares:
"""
squares	=	[x**2	for	x	in	range(0,11)]
print(squares)
"""

#ver2-a list of tuples

squares	=	[(x,	x**2,	x**3)
                 for x in range(0,9)]
print(squares)

squares	=	[(x,	x**2,	x**3)
                 for x in range(0,9)
                    if	x	%	2	==	0]
print(squares)


#The initial expression in the list comprehension can be anything, even another list  comprehension
d = [[x*y	for	x in range(1,5)] for y in range(1,5)]
print(d)