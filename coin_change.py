lst=list(map(int,input().split()))
def house(lst):
    m=0
    n=0
    if len(lst)<2:
        return(lst[0])
    if len(lst)==2:
        return(max(lst))
    if len(lst)==3:
        m=lst[0]+lst[2]
        n=lst[2]
        return(m if m>n else n)
    for i in range(0,len(lst)//2-1):
        if(len(lst)%2==0):
            m=lst[i]+lst[i+2]+m
            n=lst[i+1]+lst[i+3]+n
        if(len(lst)%2!=0):
            m=lst[i]+lst[i+2]+lst[i+4]+m
            n=lst[i+1]+lst[i+3]+n
    return(m if m>n else n)
print(house(lst))
