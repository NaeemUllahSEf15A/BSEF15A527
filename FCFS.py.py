def main():
    total=int(input("Enter total nuumber of process"))
    arrival =[]
    burst = []
    turnarount = []
    waiting = []

    for i in range(total):
        arr=int(input("Enter Arrival Time"))
        arrival.append(arr)

    for k in range(total):
        bur=int(input("Enter Burst Time"))
        burst.append(bur)

    finishtime = [0] * total
    finishtime[0]=arrival[0]+burst[0]
    for j in range (1,total):
        finishtime[j]=finishtime[j-1]+burst[j]

    Starttime=[0] * total
    Starttime[0]=arrival[0]
    for l in range(1,total):
        Starttime[l] = finishtime[l-1]

    waitingtime = 0
    for p in range(total):
        waiting[p] = Starttime[p] - arrival[p]
        waitingtime += waiting[p]
    avgwaiting = waitingtime / total

    print("processes \t arrival time \t burst time \t start time \t finishtime \t")
    for n in range(total):
        print("p",n,"\t\t\t\t",arrival[n],"\t\t\t\t",burst[n],"\t\t\t\t",Starttime[n],"\t\t\t\t",finishtime[n])



main()