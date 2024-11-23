# Write a function to find the number of tallest candles on a birthday cake

def tallest_candle(candles):

    tallest = max(candles)
    return candles.count(tallest)

candles = [4,4,1,3]
print(tallest_candle(candles))
