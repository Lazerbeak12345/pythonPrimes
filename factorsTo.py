import sys
factorTo=int(sys.argv[1])
found=[]
for factor in range(factorTo+1):
    print(factor,end=":\t")
    output=[]
    current=2
    while factor>=current:
        isNotPrime=False
        for number in found:
            isNotPrime=number**2<=current and current%number==0
            if isNotPrime:
                break
        if not isNotPrime:
            if found==[] or found[-1]<current:
                found.append(current)
            count=0 # Number of times current is inside factor
            while factor%current==0:
                count+=1
                factor=factor/current # if this is no-whole, something went wrong
            if count>0:
                output.append((current,count))
        current+=1
    strOut=[]
    for number,count in output:
        if count>1:
            strOut.append(f"({number}**{count})")
        else:
            strOut.append(number)
    print(*strOut,sep="*")
print(*found,sep=", ")
