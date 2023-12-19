import re


def is_day_valid(day: str) -> bool:
    if not day.isdecimal():
        return False

    int_day = int(day)
    return int_day >= 1 and int_day <= 31


def is_int_month_valid(month: int) -> bool:
    return month >= 1 and month <= 12


def is_string_month_valid(month: str) -> bool:
    return month in months


def is_month_valid(month: str) -> bool:
    is_valid = False

    if month.isdecimal():
        is_valid = is_int_month_valid(int(month))
    else:
        is_valid = is_string_month_valid(month)

    return is_valid


def is_year_valid(year: str) -> bool:
    return year.isdecimal()


def is_date_input_valid(day: str, month: str, year: str) -> bool:
    return is_day_valid(day) and is_month_valid(month) and is_year_valid(year)


def convert_month_to_number(month: str) -> int:
    if month.isdecimal():
        return int(month)

    return months.index(month) + 1


def unify_date(day: str, month: str, year: str) -> tuple[int, int, int]:
    return (int(day), convert_month_to_number(month), int(year))


months = [
    "январь",
    "февраль",
    "март",
    "апрель",
    "май",
    "июнь",
    "июль",
    "август",
    "сентябрь",
    "октябрь",
    "ноябрь",
    "декабрь",
]


# По какой-то причине на вход подаётся в том числе и предикат echo "-e"
def process_date_input(date_input: str) -> tuple[str, str, str]:
    split = re.split("[\\.\\s]", date_input, 3)
    if len(split) > 3:
        return (split[1], split[2], split[3])

    return (split[0], split[1], split[2])


while True:
    date_input = input("Дата: ").strip()
    day_input, month_input, year_input = process_date_input(date_input)

    if not is_date_input_valid(day_input, month_input, year_input):
        continue

    day, month, year = unify_date(day_input, month_input, year_input)
    print(f"{year}-{month:02}-{day:02}")
    break
