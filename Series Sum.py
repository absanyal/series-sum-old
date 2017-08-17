f = open("data1.txt","w")
z = 0.001
s = 0.0
n = 0
c = 1/(1-z)

e = (c-s)/c

while (z<1):
    while (e > 0.0001):
        s = s + z**n
        n = n +1
        e = (c-s)/c
    print("z = ",round(z,10))
    print("Calculated sum from series: ", round(s,10))
    print("Calculated sum from formula: ", round(c,10))
    print("Percentage of error: ", round((e*100),10))
    print("Number of terms needed: ", n+1)
    print("*"*10)
    p = str(round(z,10)) + "\t" + str(n+1) + "\n"
    f.write(p)
    z = z + 0.001
    c = 1/(1-z)
    s = 0.0
    n=0
    e = (c-s)/c
f.close()
