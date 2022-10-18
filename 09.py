# Разработайте программу, которая проверяет, что все цифры, которые входят в
# заданное натуральное число, являются нечётными.


def find_odd_digits(num):
    while num > 0:
        n1 = num % 10

        if n1 % 2 == 0:
            result = False
            break
        else:
            result = True

        num //= 10

    return result


def main():
    num = int(input("Input your number: "))
    msg = f"All digits of your number are odd: {find_odd_digits(num)}"

    print(msg)


main()