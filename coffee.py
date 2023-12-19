def print_remaining_sum(price_per_coffee: int, total_inserted: int):
    print("Нужная сумма:", price_per_coffee - total_inserted)


price_per_coffee = 50
total_inserted = 0
allowed_coins = {"50", "20", "10", "5"}

while total_inserted < price_per_coffee:
    print_remaining_sum(price_per_coffee, total_inserted)

    coin = input("Вставьте монету: ")

    if coin in allowed_coins:
        total_inserted += int(coin)


owe = total_inserted - price_per_coffee
print(f"Ваша сдача: {owe}")
