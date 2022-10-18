# Разработайте программу, которая проверяет, что все цифры заданного нату-
# рального числа различны

def find_inequality(num):
    while num != 0:
        n1 = num % 10
        ls = list(str(num // 10))

        if str(n1) in ls:
            answer = False
            break
        else:
            answer = True

        num //= 10

    return answer


def main():
    num = int(input("Imput your number: "))
    msg = f"{find_inequality(num)}"

    print(msg)


main()
