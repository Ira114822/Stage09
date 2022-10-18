# Разработайте программу, которая проверяет, что заданное натуральное число
# читается одинаково слева направо и справа налево (т.е. является палиндро-
# мом).


num = int(input("Input your number: "))
x = len(str(num))
i = 0
x = x - 1
k = 0
while x - i >= i:
    if str(num)[x - i] == str(num)[i]:
        i += 1
    else:
        k = 1
        break
if k == 1:
  print("no")
else:
  print("yes")