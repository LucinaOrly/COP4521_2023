#Acessing strings
"""
s1 = "This is a string!"
s2 = "Python is so awesome."

print(s1[3])
print(s2[5:15])
"""

#Modifying strings
"""
s1 = "Python is so awesome."
print(s1)
s1 = "Python is so cool."
print(s1)
"""

"""
s1 = "Python is so awesome."
print(s1)
s1 = s1[:13]+"cool."
print(s1)
"""

"""
s1 = "Python is so awesome."
print(s1.upper())
print(s1.lower())
"""

"""
print("WHOA".isupper())
print("12345".isdigit())
print("	\n	".isspace())
print("hello!".isalpha())
"""

"""
print("Python	programming	is	fun!".split())
print("555-867-5309".split('-'))
print("***Python	programming	is	fun***".strip('*'))
"""

"""
print("i	LoVe	pYtHoN".capitalize())
print("centered".center(20,'*'))
print("mississippi".count("iss"))
print("mississippi".count("iss", 4, -1))
print("mississippi".endswith("ssi"))
print("mississippi".endswith("ssi", 0, 8))
"""

"""
print("whenever".find("never"))
print("whenever".find("what"))
print("whenever".index("never"))
#print("whenever".index("what"))
"""

"""
print("-".join(['555','867','5309']))
print("	".join(['Python',	'is',	'awesome']))
print("whenever".replace("ever",	"ce"))
"""