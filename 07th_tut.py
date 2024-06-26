# Strings in python
name = 'Barsat'
surname = 'Rai'
college = 'HCOE'
print("Hello, "+name+surname,'school:',college)
string = '''
hello, guys im learning python program'''
print(string)
print(name[3],len(string),len(college))
print(string[7])

#string operations
## slicing
names = 'barsat,suvam,Anya,Kennedy'
print(name[0:6],len(names))
name = "python"
print("the total length of python is:",len(name),'okay?')
print(name[1:-2])  #[start:end]
print(name[:-2])
print(name[-2])
print(name[-4:-2])
# n

#String methods
#---strings are immutable
a = "Barsa!!!!!!!!!!!!!"
print(a.upper())
print(a.lower())
print(len(a))
print(a.rstrip("t")) #strips tailing characters
print(a.replace("Barsa","norma"))
print(a.split(" "))
b = 'i loVe you'
print(b.capitalize()) # first letter capital and remaining in small

print(len(b))
print(len(b.center(20)))
print(b.count("o"))
str1 = 'welcome to my profile'
print(str1.endswith("e"))
print(str1.endswith("e",4,5))

str2 = "I'm a good boy"
print(str2.find("good"))
print(str2.find(a))
print(str2.isalnum()) # if string contain 0-1, A-Z, a-z return true else false
print(str2.islower())
print(str2.isprintable())   #printable in console 
print(str2.isspace()) #return true only string contain white space
print(str2.istitle()) #return true only if all first letter in strin is capital
print(str2.swapcase()) # upper to lower and vice-versa
print(str2.title()) # converts to title case


