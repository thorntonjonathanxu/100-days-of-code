def get_max_profit(lst:list) -> int:
    max = 0
    for i in lst:
        for j in lst:
            if i - j < max:
                max = i - j

    return max * -1



stock_prices = [10, 7, 5, 8, 11, 9]

print(get_max_profit(stock_prices))
# Returns 6 (buying for $5 and selling for $11)

