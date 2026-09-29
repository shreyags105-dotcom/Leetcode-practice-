def max_profit(prices):
    if not prices:
        return 0

    min_price = prices[0]
    best_profit = 0

    for price in prices[1:]:
        if price < min_price:
            min_price = price
        else:
            best_profit = max(best_profit, price - min_price)

    return best_profit


if __name__ == "__main__":
    assert max_profit([7, 1, 5, 3, 6, 4]) == 5
    assert max_profit([7, 6, 4, 3, 1]) == 0
    assert max_profit([1, 2]) == 1
    print("Best Time to Buy and Sell Stock tests passed.")
