x=int(input("Enter lower limit:"))
y=int(input("Enter upper limit:"))
for i in range(x,y+1):
    if i%2==0:
        print(i,"-> EVEN")
    else:
        print(i,"-> ODD")