import sys
factor=int(sys.argv[1])
output=[]
found=[]
current=2
while factor>=current:
    # print(f"current: {current}")
    isNotPrime=False
    for number in found:
        isNotPrime=number**2<=current and current%number==0
        if isNotPrime:
            break
    if not isNotPrime:
        found.append(current)
        count=0
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
print(*found,sep=", ")
print(*strOut,sep="*")
