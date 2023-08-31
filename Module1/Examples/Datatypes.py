# single line comment




#datatypes

x = int(4.6)
print(x)
x = float(4)
print(x)
x = -12.6
print(x)
x = abs(-12.6)
print(x)
x = 6/4
print(x)
x = int(6/4)
print(x)
x = 6%4
print(x)


#SEQUENCE TYPES - STRINGS

txt = "My name is Karen Works"
print(txt)
txt = "My name is \nKaren \t Works"
print(txt)
print("My name is \n"+"Karen \t Works")


#unicode

myunicodestr1 = u"Hi Class!"
myunicodestr2 = u"Hi\u0020Class!"
print (myunicodestr1, myunicodestr2)
newunicode = u'\xe4\xf6\xfc'
print(newunicode)
newstr = newunicode.encode('utf-8')
print(newstr)
print(newstr.decode('utf-8'))


#lists

mylist = [42, 'apple', u'unicode apple', 5234656]
print(mylist)
mylist[2] = 'banana'
print(mylist)
mylist[3] = [['item1', 'item2'], ['item3', 'item4']]
print (mylist)
print(mylist.pop())
mynewlist = [x*2 for x in range(0,5)]
print(mynewlist)

mylist = [4,1,3,2]
print(mylist)
mylist.sort()
print(mylist)


#more seq datatypes

mylist = ["spam", "eggs", "toast"] # List of strings!
print("eggs" in mylist)
print(len(mylist))
mynewlist = ["coffee", "tea"]
print(mylist + mynewlist)
mytuple = tuple(mynewlist)
print(mytuple)
print(mytuple.index("tea"))
mylonglist = ['spam', 'eggs', 'toast', 'coffee', 'tea']
print(mylonglist[2:4])


#sets

basket = ['apple', 'orange', 'apple', 'pear', 'orange']
fruit = set(basket)
print(fruit)
print('orange' in fruit)
print('crabgrass' in fruit)
a = set('abracadabra')
b = set('alacazam')
print(a)
print(a - b)
print(a | b)


#Dict

gradebook = dict()
gradebook['Susan Student'] = 87.0
print(gradebook)
gradebook['Peter Pupil'] = 94.0
print(gradebook.keys())
print(gradebook.values())
print(gradebook.__contains__('Tina Tenderfoot'))
gradebook['Tina Tenderfoot'] = 99.9
print(gradebook.__contains__('Tina Tenderfoot'))
print(gradebook)
gradebook['Tina Tenderfoot'] = [99.9, 95.7]
print(gradebook)

