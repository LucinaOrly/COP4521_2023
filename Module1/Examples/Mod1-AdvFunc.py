#FUNCTION Closures
"""
def	make_inc(x):
    def	inc(y):
        #	x	is	closed	in
        #	the	definition	of	inc
        return	x	+	y
    return	inc

inc5	=	make_inc(5)
inc10	=	make_inc(10)

print(inc5(5))	#	returns	10
print(inc10(5))	#	returns	15
"""

#DECORATORS

#ver1
"""
def	say_hello(name):
    return	"Hello,	"	+	str(name)	+	"!"

def	p_decorate(func):
    def	func_wrapper(name):
        return	"<p>"	+	func(name)	+	"</p>"
    return	func_wrapper

my_say_hello=p_decorate(say_hello)
print(my_say_hello("John"))
"""

#ver 2
"""
def	p_decorate(func):
    def	func_wrapper(name):
        return	"<p>"+func(name)+"</p>"
    return	func_wrapper

@p_decorate
def	say_hello(name):
    return	"Hello,	"+str(name)+"!"

print(say_hello("John"))
"""


#ver 3
"""
def	div_decorate(func):
    def	func_wrapper(name):
        return	"<div>"+func(name)+"</div>"
    return	func_wrapper

def	p_decorate(func):
    def	func_wrapper(name):
        return	"<p>"+func(name)+"</p>"
    return	func_wrapper

def	strong_decorate(func):
    def	func_wrapper(name):
        return	"<strong>"+func(name)+"</strong>"
    return	func_wrapper

@div_decorate
@p_decorate
@strong_decorate
def	say_hello(name):
    return	"Hello,	"+str(name)+"!"

print(say_hello("John"))
"""

#ver 4
"""
def	tags(tag_name):
    def	tags_decorator(func):
        def	func_wrapper(name):
            return	"<"+tag_name+">"+func(name)+"</"+tag_name+">"
        return	func_wrapper
    return	tags_decorator

@tags("p")
def	say_hello(name):
    return	"Hello,	"	+	str(name)	+	"!"

print(say_hello("John"))	#	Output	is:	<p>Hello,	John!</p>
"""

#accepts example
#ver 1
"""
import	math

def	complex_magnitude(z):
    return	math.sqrt(z.real**2	+	z.imag**2)

#print(complex_magnitude("hello"))
print(complex_magnitude(1+2j))
"""

#ver 2
"""
import	math

def	accepts(*arg_types):
    def	arg_check(func):
        def	new_func(*args):
            for	arg,	arg_type	in	zip(args,arg_types):
                if	type(arg)	!=	arg_type:
                    print("Argument",	arg,	"is	not	of	type",	arg_type)
                    break
                else:
                    func(*args)
        return	new_func
    return	arg_check

@accepts(complex)
def complex_magnitude(z):
    print(math.sqrt(z.real ** 2 + z.imag ** 2))

print(complex_magnitude("hello"))
print(complex_magnitude(1+2j))
"""