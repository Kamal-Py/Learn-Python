
#* Operators:

a = 12
b = 3

print(a + b)    # 15
print(a - b)    # 9
print(a * b)    # 36
print(a / b)    # 4.0
print(a // b)   # 4 integer division, rounded down toward minus infinity
print(a % b)    # 0 module: the remainder after integer division

print()


#* Operator Precedence:
# (PEMDAS) Parentheses, Exponents, Multiplication/Division, Addition/Subtraction
# (BEDMAS) Brackets, Exponents, Division/Multiplication, Addition/Subtraction
# (BODMAS) Brackets, Order, Division/Multiplication, Addition/Subtraction 
# (BIDMAS) Brackets, Index, Division/Multiplication, Addition/Subtraction

#! Multiplication and Division have equal precedence
#! Addition and Subtraction have equal precedence

print(a + b / 3 - 4 * 12)
print(a + (b / 3) - (4 * 12))
print((a + b) / (3 - 4) * 12)
print(((a + b) / 3 ) - 4 * 12)

c = a + b
d = c / 3
e = d - 2
print(e * 10)

print()
print(a / (b * a) / b)
