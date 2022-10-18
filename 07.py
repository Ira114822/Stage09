# Разработайте программу, которая с использованием эффективного алгоритма
# находит максимальную цифру заданного натурального числа.

def find_max_digit(num):
    max_digit = num % 10

    while num != 0:
        num //= 10
        n1 = num % 10
        if n1 > max_digit:
            max_digit = n1

    return max_digit


def main():
    num = int(input("Input your number: "))

    msg = f"Max digit of your number is {find_max_digit(num)}"

    print(msg)


main()
