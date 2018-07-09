def maxprofit (prices):
    max=0
    m=0
    n=0
    for i in range (0,len(prices)):
        for j in range (i, len(prices)):
            if max<(prices[j]-prices[i]):
                max=prices[j]-prices[i]
                m=j
                n=i
    return max
