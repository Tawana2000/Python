# Write a function to return the buy and sell prices from a list of daiuly stock prices

def maximize_profit(prices):
    min_price, max_profit = float('inf'), 0
    buy, sell = 0, 0

    for price in prices:
        if price < min_price:
            min_price = price
        if price - min_price > max_profit:
            max_profit = price - min_price
            buy, sell = min_price, price

    return (buy, sell)


prices = [100, 180, 260, 310, 40, 535, 695]
print(maximize_profit(prices))