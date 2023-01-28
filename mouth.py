# Decision task
def countDays(_days: int):
    _dayValueCount = 0
    _dayCollection = []
    for value in range(1, _days + 1):
        _dayCollection.append(str(value))
    for element in _dayCollection:
        if len(element) == 2:
            _dayValueCount += int(element[0]) + int(element[1])
        else:
            _dayValueCount += int(element)
    return _dayValueCount

# Beautiful print results
def PrintMathInfo(_text: str, _year: dict):
    _sumNumberYear = 0
    print(_text)
    for dates in _year:
        print(f"Название месяца: {dates}; Результат подсчёта: {countDays(_year[dates])}")
        _sumNumberYear += countDays(_year[dates])
    print(f"Результат подсчёта:\t{_sumNumberYear}")
    return _sumNumberYear


# Task input
simpleYear = {"January": 31, "February": 28, "March": 31, "April": 30, "May": 31,
        "June": 31, "July": 30, "August": 31, "September": 30,
        "October": 31, "November": 30, "December": 31}

highYear = {"January": 31, "February": 29, "March": 31, "April": 30, "May": 31,
            "June": 30, "July": 31, "August": 31, "September": 30,
            "October": 31, "November": 30, "December": 31}

# Task action
try:
    Answer = int(input("Исходя из какого месяца сделать вычисления: \n1)Обычный год\n2)Високосный год\nОтвет:\t"))
    match (Answer):
        case 1:
            PrintMathInfo("Обычный год:", simpleYear)
        case 2:
            PrintMathInfo("Високосный год:", highYear)
        case _:
            print("Подобного действия нету!")
except:
    print("Подобного действия нету!")
