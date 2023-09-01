#string constants
"""
import	string
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.digits)
print(string.hexdigits)
"""

"""
import	string
print(string.ascii_lowercase)
print(string.ascii_uppercase)
print(string.ascii_letters)
print(string.octdigits)
print(string.punctuation)
"""

#string format
"""
print('{0}{1}{2}'.format('a','b','c'))
print('{}{}{}'.format('a','b','c'))
print('{2}{1}{0}'.format('a','b','c'))
print('{2}{1}{0}'.format(*'abc'))
print('{0}{1}{0}'.format('abra',	'cad'))
"""

#format
"""
print('Coords:	{lat},	{long}'.format(lat='37.24N',	long='-115.81W'))
coord	=	{'lat':	'37.24N',	'long':	'-115.81W'}
print('Coords:	{lat},	{long}'.format(**coord))
"""

#format
"""
c	=	2+3j
print('{0}	has	real	part	{0.real}	and	imaginary		part	{0.imag}.'.format(c))
coord	=	(3,	5)
print('X:	{0[0]};	Y:	{0[1]}'.format(coord))
"""

"""
print('{:<30}'.format('left	aligned'))
print('{:>30}'.format('right	aligned'))
print('{:^30}'.format('centered'))
print('{:*^30}'.format('centered'))
"""

#show sign
print('{:+f};	{:+f}'.format(3.14,	-3.14))
#show space for +
print('{: f};	{: f}'.format(3.14,	-3.14))
#show only -
print('{:-f};	{:-f}'.format(3.14,	-3.14))
#limit to 3 decimal places
print('{:.3f}'.format(3.14159))
