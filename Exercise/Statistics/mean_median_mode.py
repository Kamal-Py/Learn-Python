# Mean, Median, Mode

#* Mean 

N = int(input(""))
X = [i for i in input().strip().split(" ")]

add = 0
for i in X:
    add += int(i)

mean = add/N
print(mean)


#* Median:
# 10 - 
# 9 -

int_x = []
for _ in X:
    int_x.append(int(_))


sorted_value = sorted(int_x)
index_for_median = (N-1) / 2


if N % 2 == 0:
    median = (sorted_value[int(index_for_median-0.5)]+sorted_value[int(index_for_median+0.5)])/2
    print(median)
else:
    median = sorted_value(int(index_for_median))
    print(median)


#* Mode

frequency_dict = {}

for number in sorted_value:
    if number in frequency_dict:
        frequency_dict[number] += 1
    else:
        frequency_dict[number] = 1

max_frequency = max(frequency_dict.values())

if max_frequency == 1:
    mode = [sorted_value[0]]
else:
    mode = []
    for keys, values in frequency_dict.items():
        if values == max_frequency:
            mode.append(keys)


print(mode[0])
