# Разработайте программу, которая проверяет, что цифры заданного числа
# образуют возрастающую (убывающую) последовательность



def find_pattern(num):

    while num > 0:
        n1 = num % 10
        num //= 10
        n2 = num % 10

        if n2 == 0:
            break

        if n1 < n2:
            result = "descending sequence"
        else:
            result = "value does not meet conditions"
            break

        num //= 10


    return result

def main():
    num = int(input("Input your number: "))

    msg = f"The result of checking your number: {find_pattern(num)}"

    print(msg)

main()