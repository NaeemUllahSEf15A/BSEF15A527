# BSEF15A527def main():
    total=int(input("Enter total nuumber of process"))
    arrival =[]
    burst = []
    turnarount = []
    waiting = []
    priority=[]
    pos=0

    for i in range(total):
        arr=int(input("Enter Arrival Time"))
        arrival.append(arr)

    for k in range(total):
        prio=int(input("Enter priority "))
        priority.append(prio)
        bur=int(input("Enter Burst Time"))
        burst.append(bur)

    for m in range(total):
         pos=m
         for o in range(1,total):
            if (priority[o]<priority[pos]):
              pos=o
            break





    for p in range(total):
         temp = priority[p]
         priority[i] = priority[pos]
         priority[pos] = temp
         temp = burst[p]
         burst[p] = burst[pos]
         burst[pos] = temp
         temp = arrival[p]
         arrival[i] = arrival[pos]
         arrival[pos] = temp

    finishtime = [0] * total
    finishtime[0]=arrival[0]+burst[0]
    for j in range (1,total):
        finishtime[j]=finishtime[j-1]+burst[j]

    Starttime=[0] * total
    Starttime[0]=arrival[0]
    for l in range(1,total):
        Starttime[l] = finishtime[l-1]

    print("processes \t arrival time \t burst time \t start time \t finishtime \t")
    for n in range(total):
        print("p",n,"\t\t\t\t",arrival[n],"\t\t\t\t",burst[n],"\t\t\t\t",Starttime[n],"\t\t\t\t",finishtime[n],"\t\t\t\t",priority[n])







main()
