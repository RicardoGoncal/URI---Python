# coding : utf - 8


i = 0
while (i <= 2.00):
    j = 1
    while(j <= 3):
        if i == 0.00:
            print("I=%d J=%d " % (i, j + i))
            j = j + 1
        elif i == 1.00:
            print("I=%d J=%d " %(i,j+i))
            j = j + 1
        elif i == 2.00:
            i = 2
            print("I=%d J=%d " %(i,j+i))
            j = j + 1
        else:
            print("I=%.1f J=%.1f " %(i,j+i))
            j = j + 1
    i = i + 0.2

