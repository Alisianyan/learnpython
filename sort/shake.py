sorted_list = [3, 2, 19, 18, 15, 6, 6, 5,2]
i = 1
first_sorted_element = -1
last_sorted_element = len(sorted_list)
x = last_sorted_element - 2

def change_elements_left_to_right(i, sorted_list):
    if sorted_list[i] < sorted_list[i-1]:
        tmp = sorted_list[i]
        sorted_list[i] = sorted_list[i-1]
        sorted_list[i-1] = tmp
def change_elements_right_to_left(x, sorted_list):
    if sorted_list[x+1] < sorted_list[x]:
        tmp = sorted_list[x]
        sorted_list[x] = sorted_list[x+1]
        sorted_list[x+1] = tmp

for count in range(int(len(sorted_list)/2)):
    while first_sorted_element < i < last_sorted_element:
        change_elements_left_to_right(i, sorted_list)
        i = i + 1
     
    while last_sorted_element > x > first_sorted_element:
        change_elements_right_to_left(x, sorted_list)
        x = x - 1

    last_sorted_element = last_sorted_element - 1
    first_sorted_element = first_sorted_element + 1
    i = first_sorted_element + 2
    x = last_sorted_element - 2
print(sorted_list)