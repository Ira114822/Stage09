# Написать программу, которая подсчитывает количество только чётных (или
# нечётных) цифр заданного натурального числа

def count_odd_digits(num):
    count_odd = 0
    while num > 0:
        n1 = num % 10
        if n1 % 2 > 0:
            count_odd += 1
        num //= 10

    return count_odd


def count_even_digits(num):
    count_even = 0
    while num > 0:
        n1 = num % 10
        if n1 % 2 == 0:
            count_even += 1
        num //= 10

    return count_even


def main():
    num = int(input("Input your number: "))
    result_odd = count_odd_digits(num)
    result_even = count_even_digits(num)

    msg = f"Number of odd digits  is {result_odd} and even digits is {result_even}"

    print(msg)


main()
