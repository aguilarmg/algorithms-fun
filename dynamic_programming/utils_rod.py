def genCutPrices(data):
    prices = []

    for line in data:
        """
        After calling split() on line i, `cost` should be of the form 
        [ cost_i ], where cost_i is a string.
        """
        price = line.split()
        prices.append(int(price[0]))

    return prices

def calcOptRevenue(prices, optRevenues, i):
    """
    prices: List[int]
        Contains list of prices user can charge for a rod cut of a given length.
    optRevenues: List[int]
        List containing the optimal revenue that the user can obtain by cutting
        up a rod for that given length.

    Return: int
        The optimal revenue that the user can obtain by cutting up a rod of
        length i.
    """

    if optRevenues[i]:
        return optRevenues[i]
    else:
        maxRevenue = prices[i]
        for j in range(i):
            if (prices[j]+prices[i-j-1]) > maxRevenue:
                maxRevenue = prices[j] + prices[i-j-1]
        optRevenues[i] = maxRevenue
        return optRevenues[i]
