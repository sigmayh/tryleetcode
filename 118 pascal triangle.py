def ptri(numRows):
    i=1
    p=[1]
    print(p)
    while i < numRows:
        p=[1]+[p[i]+p[i+1] for i in range (len(p)-1)]+[1]
        print (p)
        i+=1
        
