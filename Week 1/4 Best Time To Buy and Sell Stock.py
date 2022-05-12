from threading import local


def maxProfit(prices: list[int]) -> int:
    profit = 0
    minVal = prices[0]
    for i in range(len(prices)):
        profit = max(profit, prices[i] - minVal)
        minVal = min(minVal, prices[i])
    return profit
        
ll = [2,5,7,1,10, -1, 11]
print(maxProfit(ll))