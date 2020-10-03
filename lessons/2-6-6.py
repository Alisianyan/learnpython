# put your python code here
q = []
q += input()
summa_input = int(q[0])
sum_quad=0

while summa_input != 0:
    a = input()
    q.append(a)
    summa_input = summa_input + int(a)
    ##q += input()
    if summa_input == 0:
        break
for i in q:
    sum_quad = sum_quad + int(i)*int(i)
print(sum_quad)

