# Начальный вклад в банке равен 1000 руб. При ежемесячной капитализации
# через каждый месяц размер вклада увеличивается на P процентов от имеющейся суммы


def colculate_months(initial_deposit, p):
    k = 1
    s = 0
    month_plus = initial_deposit * p / 100

    while s < 2000:
        s = initial_deposit + month_plus * k
        if s <= 2000 and 0 < p < 25:
            k += 1
        else:
            break

    return k


def main():
    initial_deposit = 1000
    p = float(input("Input your interest rate: "))

    month = colculate_months(initial_deposit, p)
    s = initial_deposit + initial_deposit * (p / 100) * month

    msg = f"The size of your contribution will exceed 2000 in {month} months and will be {s}"

    print(msg)


main()
