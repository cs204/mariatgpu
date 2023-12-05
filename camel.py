user_input = input("Верблюжий стиль: ")
snake_case = ""
for char in user_input:
    if char.isupper():
        snake_case += "_" + char.lower()
    else:
        snake_case += char
print(snake_case)
