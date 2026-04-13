def coin_change(amt, coin):
    if amt < 0 or coin == 0:
        return 0
    if amt == 0 or coin == 1:
        return 1
    if coin == 5:
        return coin_change(amt - 5, 5) + coin_change(amt, 2)
    elif coin == 2:
        return coin_change(amt - 2, 2) + coin_change(amt, 1)


amount = 6
print(coin_change(amount, 5))
