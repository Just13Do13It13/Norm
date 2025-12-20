# 1. Создай две функции: inner() и outer().
# В inner() вызови деление на ноль.
# В outer() просто вызови inner().
# Попробуй вызвать outer() без обработки ошибок и посмотри на стек вызовов.
# def inner(a):
#     return a / 0
#
#
# def outer():
#     return inner(1)
#
# outer()
# 2. Добавь вокруг вызова outer() конструкцию try/except,
# чтобы перехватить исключение и вывести сообщение
# "Ошибка перехвачена на верхнем уровне".
# def inner(a):
#     return a / 0
#
#
# def outer():
#     try:
#         return inner(1)
#     except ZeroDivisionError:
#         print("Ошибка перехвачена на верхнем уровне")
#
# outer()
# 3. Перехвати исключение сразу в inner(), чтобы оно не поднималось дальше.
# В случае ошибки возвращай строку "Ошибка в inner".
# def inner(a):
#     try:
#         return a / 0
#     except ZeroDivisionError:
#         print("Ошибка в inner")
#
#
# def outer():
#     try:
#         return inner(1)
#     except ZeroDivisionError:
#         print("Ошибка перехвачена на верхнем уровне")
#
# outer()
# 4. Сделай так:
# В inner() ошибка не перехватывается.
# В outer() ошибка перехватывается через try/except.
# В outer() при перехвате напечатай "Ошибка в outer".
# def inner(a):
#         return a / 0
#
#
# def outer():
#     try:
#         return inner(1)
#     except ZeroDivisionError:
#         print("Ошибка в outer")
#
# outer()
# 5. Напиши функцию get_value(), которая кидает ValueError.
# Напиши тестовую функцию test_get_value(), которая:
#
# Вызывает get_value();
# Ловит ValueError;
# Завершает тест с assert False, если исключение поймано.
# def get_value():
#     raise ValueError("Приехали, валуееррор")
#
# def test_get_value():
#     try:
#         return get_value()
#     except ValueError:
#         assert False, "ValueError был пойман, тест не должен завершиться с ошибкой"
#     else:
#         assert True, "ValueError не был пойман, тест завершился успешно"
#
# test_get_value()
# 6. Создай функцию divide(x, y).
# Если y == 0, выбрасывай ZeroDivisionError через raise.
# Иначе возвращай результат деления.
# def divide(x, y):
#     if y == 0:
#         raise ZeroDivisionError('Опа, на ноль делить нельзя!')
#     else:
#         return x / y
#
# try:
#     print(divide(10, 2))
#     print(divide(10, 0))
# except ZeroDivisionError as e:
#     print(e)
# 7. Создай функцию sqrt(x), которая:
# Вызывает raise NegativeNumberError (пользовательское исключение), если x < 0;
# Иначе возвращает квадратный корень из x.
# Проверь поведение функции через try/except.
# class NegativeNumberError(Exception):
#     pass
# def sqrt(x):
#     if x < 0:
#         raise NegativeNumberError('X меньше нуля, расстрел')
#     else:
#         return x ** 2
#
# try:
#     print(sqrt(2))
#     print(sqrt(-2))
# except NegativeNumberError as n:
#     print(n)
    # 8. Создай базовый класс MathError.
    # От него унаследуй:
    # NegativeNumberError
    # DivisionByZeroError
    # В функции safe_divide(x, y) выбрасывай DivisionByZeroError, если y == 0.
    # Проверь в try/except обработку ошибок через базовый класс MathError.
# 8. Создай базовый класс MathError.
# От него унаследуй:
# NegativeNumberError
# DivisionByZeroError
# В функции safe_divide(x, y) выбрасывай DivisionByZeroError, если y == 0.
# Проверь в try/except обработку ошибок через базовый класс MathError.
# class MathError(Exception):
#     pass
#
# class NegativeError(MathError):
#     pass
#
# class DivisionByZeroError(MathError):
#     pass
#
# def safe_divide(x, y):
#     if y == 0:
#         raise DivisionByZeroError("y то у нас НУЛЕВЫЙ")
#     else:
#         return x / y
#
# try:
#     print(safe_divide(6, 3))
#     print(safe_divide(6, 0))
# except MathError as e:
#     print(e)
# 9. Создай тестовую функцию test_sqrt(), которая:
# вызывает sqrt(x) с отрицательным числом;
# перехватывает NegativeNumberError;
# завершает тест с assert False и сообщением
# "Нельзя брать корень из отрицательного числа".
# class NegativeNumberError(Exception):
#     pass
#
# def sqrt(x):
#     if x < 0:
#         raise NegativeNumberError("Нельзя брать корень из отрицательного числа!")
#     return x ** 0.5  # Возвращаем квадратный корень
#
# def test_sqrt():
#     try:
#         sqrt(-9)
#     except NegativeNumberError as n:
#         assert False, "Нельзя брать корень из отрицательного числа"
#
# test_sqrt()
# 10. Открой файл sample.txt, прочитай его содержимое и выведи на экран.
# Обеспечь закрытие файла через with.
# with open('sample.txt', 'r', encoding='utf-8') as f:
#     content = f.read()
# print(content)
# 11. Создай класс BackupList, который:
# делает копию списка при входе в with,
# при выходе сохраняет изменения, если ошибок не было,
# откатывает изменения при ошибке.
# Проверь:
# успешное изменение списка;
# откат при ошибке.
# class BackupList:
#     def __init__(self, original_list):
#         self.original_list = original_list
#         self.backup = None  # Для хранения резервной копии списка
#
#     def __enter__(self):
#         # Создаём резервную копию списка при входе в with
#         self.backup = self.original_list.copy()
#         return self.original_list
#
#     def __exit__(self, exc_type, exc_value, traceback):
#         # Если произошла ошибка (exc_type не None), откатываем изменения
#         if exc_type:
#             print(f"Произошла ошибка: {exc_value}. Откатываем изменения.")
#             self.original_list[:] = self.backup  # Восстанавливаем оригинальный список
#         else:
#             print("Список успешно изменён.")
#
# # Пример использования
# original_list = [1, 2, 3, 4]
#
# # Проверка успешного изменения списка
# with BackupList(original_list) as backup_list:
#     print("До изменения:", backup_list)
#     backup_list.append(5)  # Успешное изменение списка
#     print("После изменения:", backup_list)
#
# # Проверка отката изменений при ошибке
# with BackupList(original_list) as backup_list:
#     print("До ошибки:", backup_list)
#     backup_list.append(6)  # Это изменит список
#     raise ValueError("Что-то пошло не так!")  # Исключение, должен быть откат
#     print("После ошибки:", backup_list)  # Эта строка не будет выполнена
# 12. Создай декоратор-класс Timer,
# который измеряет время выполнения функции и выводит результат.
# import time
# class Timer:
#     def __init__(self, func):
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         start = time.time()
#         result = self.func(*args, **kwargs)
#         end = time.time()
#         print(f"Время выполнения {self.func.__name__}: {end - start:.6f} секунд")
#         return result
#
# @Timer
# def show_func(a, b):
#     result = a * b
#     return result
#
# print(show_func(2, 4))