
#with open ('dataset.txt') as file:
#	list = file.read().splitlines()
	
#for x in list:
#	print(x)
   
list = "a3b4c2e10b1"
list2 = []   
while True:
    for thiselem, nextelem in zip(list, list[1:] + list[:1]):
        if thiselem.isalpha():
            if nextelem.isdigit():
                