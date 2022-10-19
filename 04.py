# Разработайте программу, которая проверяет, что цифры заданного числа
# образуют возрастающую (убывающую) последовательность



TRUE_RESULT = "descending sequence"
FALSE_RESULT = "value does not meet conditions"


def find_pattern(num):

    while num > 0:
        n1 = num % 10
        num //= 10
        n2 = num % 10

        if n2 == 0:
            break

        if n1 < n2:
            result = TRUE_RESULT
        else:
            result = FALSE_RESULT
            break

        num //= 10

    return result

def main():
    num = int(input("Input your number: "))

    msg = f"The result of checking your number: {find_pattern(num)}"

    print(msg)

main()
