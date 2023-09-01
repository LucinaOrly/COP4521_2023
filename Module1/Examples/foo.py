'''	Module	foo.py'''
import	bar

print	("Hi from foo's	top	level!")

if __name__ ==	"__main__":
    print("foo's name is main")
    bar.print_hello()
