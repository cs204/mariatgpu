answer = input("Какой ответ на главный вопрос жизни, вселенной и всего такого? ")
match answer.lower():
	case "42" | "сорок два":
		print("Да")
	case _:
		print("Нет")
