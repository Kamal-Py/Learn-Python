def narcissistic( value ):
    int_value = []
    value = f"{value}"
    for i in value:
        int_value.append(int(i))
    N = len(int_value)
    print(f"N: {N}")
    value_sum = 0
    for i in int_value:
        value_sum += i ** N
    print(value_sum)
    if value_sum == int(value):
        return True
    else:
        return False # Code away

print(narcissistic(7))
print(narcissistic(371))
print(narcissistic((153)))