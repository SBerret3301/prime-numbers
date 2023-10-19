x = int(input("enter a number : "))
for i in range (1,x) :
    a = 0
    for j in range (1,i+1) :
        if i % j == 0 :
            a = a + 1
    if a == 2 :
        print(i)
