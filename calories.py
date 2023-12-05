fruit_calories = {
    "apple": 130,
    "avocado": 50,
    "banana": 110,
    "melom": 50,
    "grapefruit": 60,
    "grape": 90,
    "melon with honeydew": 50,
    "kiwi": 90,
    "lemon": 15,
    "lime": 20,
    "nectarine": 60,
    "orange": 80,
    "peach": 60,
    "pear": 100,
    "pineapple": 50,
    "plum": 70,
    "strawberry": 50,
    "sweet cherry": 100,
    "mandarin": 50,
    "watermelon": 80,

}

fruit = input("Фрукт: ").lower()

if fruit in fruit_calories:
    calories = fruit_calories[fruit]
    print(f"Калории: {calories}")
else:
    print("Фрукт не найден в списке.")
