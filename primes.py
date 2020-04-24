import sys
to=int(sys.argv[1])
found=[]
current=2
while to>=current:
    # print(f"current: {current}")
    isNotPrime=False
    for number in found:
        isNotPrime=number**2<=current and current%number==0
        if isNotPrime:
            break
    if not isNotPrime:
        found.append(current)
    current+=1
print(*found,sep="\n")
