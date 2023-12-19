menu = {
   "кофе": 20.00,
   "чай": 10.00,
   "булочка": 5.00,
   "салат": 30.40,
   "пирожное": 45.50
}

total_cost = 0.0

try:
    while True:
        dish = input("Блюдо: ").lower()

        if dish not in menu:
            # print(f"Блюдо ' {dish}' отстутсвует в меню. Продолжайте заказ." )
            continue

        total_cost += menu[dish]
except EOFError:
    print(f"\nСумма: {total_cost:.2f}")
