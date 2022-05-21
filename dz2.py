# Создать список, состоящий из кубов нечётных чисел от 1 до 1000 (куб X - третья степень числа X):
# numbers = []
# for i in range(1, 1000):
#    if i % 2 != 0:
#       numbers.append(i)
# print(numbers)
# Вычислить сумму тех чисел из этого списка,
# сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7.
# Внимание: использовать только арифметические операции!
# К каждому элементу списка добавить 17 и заново вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
numbers = [x**3 for x in range(1, 1001) if x %2 != 0]
print(numbers)
print(sum([(x**3)  for x in range(1, 1001) if x %7 == 0]))

# while x in numbers > 0:
#     x = numbers % 10
#     numbers = x + 17
# print(x)

# def sum_digits(value):
#     res = 0
#
#     while value != 0:
#         res += value % 10
#         value //= 10
#
#     return res
#
#
# arr = [i**3 for i in range(1, 1001, 2)]
#
# res1 = sum(filter(lambda num: sum_digits(num) % 7 == 0, arr))
# res2 = sum(filter(lambda num: sum_digits(num + 17) % 7 == 0, arr))
#
# print(res1)
# print(res2)

print(sum(filter(lambda j: sum(map(int, str(j))) % 7 == 0, [i**3 for i in range(1, 1001, 2)])))
print(sum(filter(lambda j: sum(map(int, str(j + 17))) % 7 == 0, [i**3 for i in range(1, 1001, 2)])))

