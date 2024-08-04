
#* About escape characters `\`: 

# \n is used to break the line 
print("This string has been\nsplit over\nseveral\nlines")

# \t is used to give tabbed space between the characters or the words
print("1\t2\t3\t4\t5")


# \ this symbol is used to delimit the string
print('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')
print("The pet shop owner said \"No, no, 'e's uh,...he's resting\".")


# Here, `"""` are used to delimit the string, allowing the multi-line strings and easier inclusion of both single and double quotes without escaping and the backslash `\` at the end of the first line is used as a line continuation character
print("""The pet shop owner said "No, no, \
'e's uh,...he's resting".""")

print("""This string has been \
split over \
several \
lines""")


# `\\` represent the single slash in the string while interpreted
print("F:\\Projects\\Python\\console_programs\\notes.txt")

# `r` prefix before the string represent string literal which tell interpreter `\` is not escape characters for this string
print(r"F:\Projects\Python\console_programs\notes.txt")