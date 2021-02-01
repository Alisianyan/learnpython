sorted_list = [2, 19, 18, 15, 6, 6, 5,2]
#sorted_list = [4, 3, 2, 1 ]

i = 1
x = 1
last_sorted_elem = len(sorted_list)
while x < len(sorted_list):
    while i <= last_sorted_elem - x:
        if sorted_list[i] < sorted_list[i-1]:
            tmp = sorted_list[i]
            sorted_list[i] = sorted_list[i-1]
            sorted_list[i-1] = tmp
        i = i+1
    x = x+1
    i = 1
print(sorted_list)
