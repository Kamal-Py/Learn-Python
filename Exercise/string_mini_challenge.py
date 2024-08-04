
#? Print out `we win` from the string `Norwegian Blue`

print("Using positive Index")
parrot = "Norwegian Blue"
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])

print("-"*5)
print("Using Negative Index")

#* Using Negative index:
print(parrot[-11])
print(parrot[-10])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])


#? Using the letters string:
# 1. Create a slice that produces the characters `qpo`
# 2. Slice the string to produce `edcba`
# 3. Slice the string to product the last 8 characters, in reverse order.
letters = "abcdefghijklmnopqrstuvwxyz"

qpo = letters[-10:-13:-1]
print(qpo)

edcba = letters[-22::-1]
print(edcba)

reversed_eight_character = letters[:-9:-1]
print(reversed_eight_character)