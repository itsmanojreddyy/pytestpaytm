inp="My name is manoj"
li=inp.split(" ")
op=""
for i in range(len(li)):
    temp=li[i]
    for j in range(len(temp)):
        # print(j)
        op=op+temp[len(temp)-j-1]
    op=op+" "
print(op)
