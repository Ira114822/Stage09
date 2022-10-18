# Разработайте программу, которая находит, сколько раз цифра 0
# (или 1, или 2,- можно выбрать любую цифру) встречается в заданном натуральном числе.

def find_count(num, digit):
    count = 0

    while num != 0:
        n1 = num % 10
        if n1 == digit:
            count +=1
        num //= 10

    return count


def main():
    num = int(input("Input your number:"))
    digit = int(input("Input your digit:"))

    msg = f"The digit {digit} is repeated in your number {find_count(num, digit)} times"

    print(msg)

main()

