str1 = "this is string for the assignment"
str2 = "THIS IS STRING FOR THE ASSIGNMENT"
str3 = "repeat is repeat in the face of youu"
str4 = "h\te\tl\tl\to"
str5 = "For only {price:.2f} dollars!"
str6 = "char45"
str7 = "156435841"
str8 = "       "
str9 = "MY!Captain!"
str10 = "          DIVYANSH          "

#Converts the first character to upper case
cap = str1.capitalize()
print(cap)

#Converts string into lower case
fold = str2.casefold()
print(fold)

#Returns a centered string
center = str1.center(100)
print(center)

#Returns the number of times a specified value occurs in a string
count = str3.count("repeat")
print(count)

#Returns an encoded version of the string
enc = str1.encode()
print(enc)

#Returns true if the string starts with the specified value
startswith = str1.startswith("assignment")
print(startswith)

#Returns true if the string ends with the specified value
endswith = str1.endswith("assignment")
print(endswith)

#Sets the tab size of the string
exptab = str4.expandtabs(5)
print(exptab)

#Searches the string for a specified value and returns the position of where it was found
find = str3.find("repeat")
print(find)

#Formats specified values in a string
print(str5.format(price = 49))

#Searches the string for a specified value and returns the position of where it was found
index = str3.index("in")
print(index)

#Returns True if all characters in the string are alphanumeric
alphanum = str6.isalnum()
print(alphanum)

#Returns True if all characters in the string are in the alphabet
alpha = str6.isalpha()
print(alpha)

#Returns True if all characters in the string are ascii characters
asc = str6.isascii()
print(asc)

#Returns True if all characters in the string are decimals
dec = str6.isdecimal()
print(dec)

#Returns True if all characters in the string are digits
digi = str7.isdigit()
print(digi)

#Returns True if the string is an identifier
iden = str7.isidentifier()
print(iden)

#Returns True if all characters in the string are lower case
chklower = str1.islower()
print(chklower)

#Returns True if all characters in the string are upper case
chkupper = str2.isupper()
print(chkupper)

#Returns True if all characters in the string are numeric
num = str7.isnumeric()
print(num)

#Returns True if all characters in the string are printable
printi = str1.isprintable()
print(printi)

#Returns True if all characters in the string are whitespaces
space = str8.isspace()
print(space)

#Returns True if the string follows the rules of a title
tit = str9.istitle()
print(tit)

#Returns a left justified version of the string
leftjust = str6.ljust(20)
print(leftjust,"hello")

#Returns a right justified version of the string
rightjust = str6.rjust(20)
print("hello",rightjust)

#Returns a trimmed version of the string
strip = str10.strip()
print(strip)

#Returns a left trim version of the string
lstrip = str10.lstrip()
print(lstrip)

#Returns a right trim version of the string
rstrip = str10.rstrip()
print(rstrip)

#Converts a string into lower case
lower = str2.lower()
print(lower)

#Converts a string into upper case
upper = str2.upper()
print(upper)

#Returns a tuple where the string is parted into three parts
part = str1.partition("for")
print(part)

#Splits the string at the specified separator, and returns a list
split = str1.split()
print(split)
