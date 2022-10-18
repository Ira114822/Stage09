# Разработайте программу, которая проверяет, что все цифры заданного натурального числа одинаковы.

def find_equality(num):

    while num > 0:
        n1 = num % 10
        num //= 10
        if num != 0:
            n2 = num % 10
            if n1 == n2:
                num //= 10
            else:
                break


    return True if n1 == n2 else False



def main():
    num = int(input("Imput your number: "))

    msg = f"{find_equality(num)}"

    print(msg)

main()
