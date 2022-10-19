# Начальный вклад в банке равен 1000 руб. При ежемесячной капитализации
# через каждый месяц размер вклада увеличивается на P процентов от имеющейся суммы


INITIAL_DEPOSIT = 1000

def colculate_month(p):
    k = 1 # количество месяцев
    s = 0   # итоговый размер вклада
    month_plus = INITIAL_DEPOSIT * p / 100

    while s < 2000:
        s = INITIAL_DEPOSIT + month_plus * k
        if s <= 2000 and 0 < p < 25:
            k += 1
        else:
            break

    return k


def main():
    p = float(input("Input your interest rate: "))

    month = colculate_month(p)
    s = INITIAL_DEPOSIT + INITIAL_DEPOSIT * (p / 100) * month

    msg = f"The size of your contribution will exceed 2000 in {month} months and will be {s}"

    print(msg)


main()
