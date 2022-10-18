# Разработайте программу, которая проверяет, что все цифры, которые входят в
# заданное натуральное число, являются чётными.

def find_even_digits(num):
    while num > 0:
        n1 = num % 10

        if n1 % 2 == 0:
            result = True
        else:
            result = False
            break

        num //= 10

    return result


def main():
    num = int(input("Input your number: "))
    msg = f"All digits of your number are even: {find_even_digits(num)}"

    print(msg)


main()
