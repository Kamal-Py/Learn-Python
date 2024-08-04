# Normal print statement with + operator to concatination the strings
from turtle import back


print("Hello" + " " + "World!")


greeting = "Hello"      # string 
name = "Kamal" 

# if we want a space, we can add that too
print(greeting + " " + name)        # string
print()



#* String Index: [Number]
#                   
# index =    01234567
bird_name = "Flamingo"
print(bird_name)
print(bird_name[3])



#* Negative index:
print()
print(bird_name[-1])
print(bird_name[-7])


#* Slicing: [Start(included):Stop(not included):Steps]
print(bird_name[0:4])
print(bird_name[3:5])
print(bird_name[0:5])
print(bird_name[5:])
print(bird_name[:])

print(bird_name[:3] + bird_name[3:])  # Norwegian Blue


#* Negative Slicing: 
print(bird_name[-7:-1])
print(bird_name[-4:])


#* Step in a Slice: (default_value = 1)
print(bird_name[::2])
print(bird_name[:4:3])

number = "9,223;372:036 854,775;807"
print(number[1::4])
seperator = number[1::4]
print(seperator)

values = "".join(char if char not in seperator else " " for char in number).split()
print([int(val) for val in values])


#* Slicing Backwards:
letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[::-1]
print(backwards)



#* String operators:
string1 = "he's "
string2 = "probably "
string3 = "Pining "
string4 = "for the "
string5 = "fjords"

print(string1 + string2 + string3 + string4 + string5)
print("he's " " probably " "pining " "for the " "fjords")
print("Hello " * 5)
print("Hello " * (5 + 4))
print("Hello " * 5 + "4")

today = "monday"
print("day" in today)
print("mon" in today)
print("tues" in today)



#* String Replacement Fields:
age = 20
print("My age is {0} years".format(age))
print("There are {0} days in {1}, {2}, {3}, {4}, {5}, {6} and {7}".format(31, "Jan", "Mar", "May", "Jul", "Aug", "Oct", "Dec"))
print("There are {0} days in Jan, Mar, May, Jul, Aug, Oct and Dec".format(31))

print("Jan: {2}, Feb: {0}, Mars: {2}, Apr: {1}, May: {2}, Jun: {1}, Jul: {2}, Aug: {1}, Sep: {1}, Oct: {2}, Nov: {1}, Dec: {2}".format(28, 30, 31))

print()

print("""Jan: {2},
Feb: {0},
Mar: {2},
Apr: {1},
Jun: {1},
Jul: {2},
Aug: {1},
Sep: {1},
Oct: {2},
Nov: {1},
Dec: {1}
""".format(28, 30, 31))



#* String Formatting:
for i in range(1, 13):
    # {0:2} Here, 0 is position index for format and 2 defines the width that will be taken by the value
    print("No. {0:2} squared is {1:4} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

for i in range(1, 13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:^4}".format(i, i**2, i**3))

print()

print("PI is approximately {0:12}".format(22/7))
print("PI is approximately {0:12f}".format(22/7))
print("PI is approximately {0:12.50f}".format(22/7))
print("PI is approximately {0:52.50f}".format(22/7))
print("PI is approximately {0:<62.50f}".format(22/7))
print("PI is approximately {0:<72.50f}".format(22/7))
print("PI is approximately {0:<72.54f}".format(22/7))

for i in range(1, 13):
    print("No. {} squared is {} and cubed is {:4}".format(i, i**2, i**3))



#* f-strings:
name = "Kamal"
age = 20
print(name + f" is {age} years old")

print(f"PI is approximately {22/7:12.50f}")

PI = 22/7
print(f"PI is approximately {PI:12.50f}")



#! Python 2 String Interpolation: (Not recommended to use in Pytohn 3)
age = 20
print("My age is %d years" % age)

major = "years"
minor = "months"
# print("My age is %d %s, %d %s" (age, major, 6, minor))
print("PI is approximately %f" % (22/7))
print("PI is approximately %60.50f" % (22/7))