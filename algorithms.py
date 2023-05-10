# def array_search(a, n, x):
#     """
#     Осуществляет поиск числа х в массиве а от 0 до n-1
#     индекса включительно. Возвращает индекс элемента х в массиве а.
#     Или -1 если такого нет.
#     Если в массиве несколько одинаковых элементов равных х,
#     то вернуть индекс первого равного по счету.
#     """
#     for i in range(n):
#         if a[i] == x:
#             return i
#     return -1


# def insert_sort(a):
#     """ Сортировка списка а вставками. """
#     n = len(a)
#     for top in range(1, n):
#         k = top
#         while k > 0 and a[k-1] > a[k]:
#             a[k], a[k-1] = a[k-1], a[k]
#             k -= 1
#
#
# def choice_sort(a):
#     """ Сортировка списка а выбором."""
#     n = len(a)
#     for pos in range(0, n-1):
#         for k in range(pos+1, n):
#             if a[k] < a[pos]:
#                 a[k], a[pos] = a[pos], a[k]
#
#
# def bubble_sort(a):
#     """ Сортировка списка а методом пузырька."""
#     n = len(a)
#     for bypass in range(1, n):
#         for k in range(0, n-bypass):
#             if a[k] > a[k+1]:
#                 a[k], a[k+1] = a[k+1], a[k]


#  Рекурсии
# def factorial(n: int):
#     """ Находит факториал. """
#     assert n >= 0, 'Факториал не определён.'
#     if n == 0:
#         return 1
#     return factorial(n - 1) * n


# def gcd(a, b):
#     """ Алгоритм Евклида. Находит наибольший общий делитель """
#     if b == 0:
#         return a
#     else:
#         return gcd(b, a % b)


# def pow(a: float, n: int):
#     """ Быстрое возведение в степень (степень - целое положительное число)"""
#     if n == 0:
#         return 1
#     elif n % 2 == 1:  # n - нечетное
#         return pow(a, n - 1) * a
#     else:  # n - четное
#         return pow(a ** 2, n // 2)


# Генерация всех перестановок. Упрощенно
# def generate_number(n: int, m: int, prefix=None):
#     """ Генерирует все числа (с лидирующими незначащими нулями)
#         в n-ричной системе счисления (n <= 10)
#         длины М
#     """
#     prefix = prefix or []
#     if m == 0:
#         print(prefix)
#         return
#     for digit in range(n):
#         prefix.append(digit)
#         generate_number(n, m - 1, prefix)
#         prefix.pop()


# def gen_bin(m, prefix=""):
#     """ Генерирует все числа (с лидирующими незначащими нулями)
#         в двоичной системе счисления длины М
#     """
#     if m == 0:
#         print(prefix)
#         return
#     gen_bin(m - 1, prefix + "0")
#     gen_bin(m - 1, prefix + "1")


# Генерация всех перестановок. Полная
# def find(number, a):
#     """
#         Ищет number в a и возвращает True, если такой есть.
#         False, если такого нет.
#     """
#     flag = False
#     for x in a:
#         if number == x:
#             flag = True
#             break
#     return flag
# ...Продолжение...
# def generate_permutations(n: int, m: int = -1, prefix=None):
#     """ Генерация всех перестановок n чисел в m позициях,
#         с префиксом prefix.
#     """
#     m = n if m == -1 else m  # по умолчанию n чисел в n позициях
#     prefix = prefix or []
#     if m == 0:
#         print(prefix)  # либо в одну строчку через запятую: print(*prefix, end=", ", sep="")
#         return
#     for number in range(1, n + 1):
#         if find(number, prefix):
#             continue
#         prefix.append(number)
#         generate_permutations(n, m - 1, prefix)
#         prefix.pop()


# Сортировка слиянием
# def merge(a: list, b: list):
#     """ Слияние отсортированных массивов. i - индекс массива a, k - индекс массива b, n - индекс доп. массива c. """
#     c = [0] * (len(a) + len(b))
#     i = k = n = 0
#     while i < len(a) and k < len(b):
#         if a[i] <= b[k]:
#             c[n] = a[i]
#             i += 1
#             n += 1
#         else:
#             c[n] = b[k]
#             k += 1
#             n += 1
#     while i < len(a):
#         c[n] = a[i]
#         i += 1
#         n += 1
#     while k < len(b):
#         c[n] = b[k]
#         k += 1
#         n += 1
#     return c


# Сортировка Тони Хоара.
# def hoar_sort(a):
#     if len(a) <= 1:
#         return
#     barrier = a[0]
#     l = []
#     m = []
#     r = []
#     for x in a:
#         if x < barrier:
#             l.append(x)
#         elif x == barrier:
#             m.append(x)
#         else:
#             r.append(x)
#     hoar_sort(l)
#     hoar_sort(r)
#     k = 0
#     for x in l + m + r:
#         a[k] = x
#         k += 1


# def check_sorted(a, ascending=True):
#     """ Проверка отсортированности массива (по умолчанию восходящего,
#         при убывающем указать во втором параметре True).
#     """
#     flag = True
#     n = len(a)
#     s = 2 * int(ascending) - 1
#     for i in range(0, n - 1):
#         if s * a[i] > s * a[i + 1]:
#             flag = False
#             break
#     return flag
