# 1. Создай три класса: Cat, Dog, Duck.
# В каждом реализуй метод speak(), возвращающий уникальную строку.
# Создай список из экземпляров этих классов и вызови метод speak()
# в цикле.
# class Cat:
#     def speak(self):
#         return "Кот: мяу"
#
#
# class Dog:
#     def speak(self):
#         return "Собака: гав"
#
#
# class Duck:
#     def speak(self):
#         return "Утка: кря"
#
# animals = [Cat(), Dog(), Duck()]
#
# for animal in animals:
#     print(animal.speak())
# 2. Создай базовый класс Shape
# Создай три класса-наследника: Square, Rectangle, Triangle,
# в каждом реализуй метод get_pr().
# Проверь, что список shapes = [Square(...), Rectangle(...), Triangle(...)]
# можно обойти в цикле и вызвать get_pr() у каждого.
# class Shape:
#     def get_pr(self):
#         return 0
#
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def get_pr(self):
#         return 4 * self.side
#
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def get_pr(self):
#         return 2 * (self.width + self.height)
#
#
# class Triangle(Shape):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def get_pr(self):
#         return self.a + self.b + self.c
#
#
# shapes = [
#     Square(5),
#     Rectangle(4, 6),
#     Triangle(3, 4, 5)
# ]
#
# for shape in shapes:
#     print(shape.get_pr())
# 3. Сделай класс Shape абстрактным.
# Переопредели get_pr() как @abstractmethod.
# Попробуй создать объект класса Shape напрямую и убедись, что будет TypeError.
# from abc import ABC, abstractmethod
#
#
# class Shape(ABC):
#
#     @abstractmethod
#     def get_pr(self):
#         pass
#
#
# class Square(Shape):
#     def __init__(self, side):
#         self.side = side
#
#     def get_pr(self):
#         return 4 * self.side
#
#
# # Проверка
# # shape = Shape()        # ❌ TypeError
# sq = Square(5)
# print(sq.get_pr())       # 20
# 4. Создай классы A, B, C, в каждом — свой __init__() с print("init A/B/C").
# Наследуй D(A, B, C) и вызови super().__init__() в каждом __init__.
# Выведи D.__mro__ и посмотри, в каком порядке вызываются инициализаторы.
# class A:
#     def __init__(self):
#         print("init A")
#         super().__init__()
#
# class B:
#     def __init__(self):
#         print("init B")
#         super().__init__()
#
# class C:
#     def __init__(self):
#         print("init C")
#         super().__init__()
#
# class D(A, B, C):
#     def __init__(self):
#         print("init D")
#         super().__init__()
#
# d = D()
# print(D.__mro__)
# 5. Создай MixinLog (как в уроке).
# Создай класс бронирования гостиницы (методы и атрибуты на свое усмотрение).
# Создай класс, который наследует оба класса. Создай экземпляр этого класса.
# import datetime
#
# class MixinLog:
#     ID = 0
#
#     def __init__(self):
#         MixinLog.ID += 1
#         self.id = MixinLog.ID
#
#     def save_sell_log(self):
#         print(
#             f"{self.id} продан в "
#             f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
#         )
#
#
# class HotelBooking:
#     def __init__(self, guest_name, nights):
#         self.guest_name = guest_name
#         self.nights = nights
#
#     def book(self):
#         print(f"Бронирование для {self.guest_name} на {self.nights} ночей")
#
#
# class LoggedHotelBooking(MixinLog, HotelBooking):
#     def __init__(self, guest_name, nights):
#         MixinLog.__init__(self)
#         HotelBooking.__init__(self, guest_name, nights)
#
#
# booking = LoggedHotelBooking("Daniil", 3)
# booking.book()
# booking.save_sell_log()
# 6. В Goods и MixinLog реализуй print_info().
# Создай NoteBook(Goods, MixinLog) и проверь, какой метод вызывается.
# Измени порядок наследования — изменилась ли логика?
# class MixinLog:
#     def print_info(self):
#         print("Информация из MixinLog")
#
#
# class Goods:
#     def print_info(self):
#         print("Информация из Goods")
#
#
# class NoteBook(Goods, MixinLog):
#     pass
#
#
# nb = NoteBook()
# nb.print_info()
# print(NoteBook.__mro__)
# 7. Напиши программу, которая запрашивает (из консоли) два числа и делит первое на второе.
# Если второе число равно нулю — обработай ошибку (как называется ошибка найди сам)
# и выведи сообщение: "На ноль делить нельзя!"
# a = int(input("Первое число: "))
# b = int(input("Второе число: "))
#
# try:
#     result = a / b
#     print(result)
# except ZeroDivisionError:
#     print("На ноль делить нельзя!")
# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return "На ноль делить нельзя!"
#
# a = int(input("Первое число: "))
# b = int(input("Второе число: "))
#
# print(divide(a, b))
# class Divider:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def divide(self):
#         try:
#             return self.a / self.b
#         except ZeroDivisionError:
#             return "На ноль делить нельзя!"
#
#
# a = int(input("Первое число: "))
# b = int(input("Второе число: "))
#
# divider = Divider(a, b)
# print(divider.divide())
# 8. Расширь программу из Задания 1:
# Добавь обработку ошибки (как называется ошибка найди сам),
# если пользователь ввёл не числа, а текст.
# Выведи сообщение: "Ошибка ввода: введите два числа через пробел"
# class Divider:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def divide(self):
#         try:
#             return self.a / self.b
#         except ZeroDivisionError:
#             return "На ноль делить нельзя!"
#
# try:
#     a = int(input("Первое число: "))
#     b = int(input("Второе число: "))
#     divider = Divider(a, b)
#     print(divider.divide())
#
# except ValueError:
#     print("Ошибка ввода: введите два числа")
# 9. Модифицируй код так, чтобы после обработки конкретных ошибок
# был ещё один общий except, который перехватывает все остальные ошибки и выводит:
# "Произошла неизвестная ошибка"
# class Divider:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def divide(self):
#         try:
#             return self.a / self.b
#         except ZeroDivisionError:
#             return "На ноль делить нельзя!"
#
# try:
#     a = int(input("Первое число: "))
#     b = int(input("Второе число: "))
#     divider = Divider(a, b)
#     print(divider.divide())
#
# except ValueError:
#     print("Ошибка ввода: введите два числа")
#
# except Exception:
#     print("Произошла неизвестная ошибка")
# 10. При перехвате исключений из 7 и 8 заданий,
# сохрани ошибку в переменную e и выведи её текст:
# class Divider:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def divide(self):
#         try:
#             result = self.a / self.b
#         except ZeroDivisionError as e:
#             e = "На ноль делить нельзя!"
#             return e
#         else:
#             return result
#
# try:
#     a = int(input("Первое число: "))
#     b = int(input("Второе число: "))
#     divider = Divider(a, b)
#     print(divider.divide())
#
# except ValueError as e:
#     print(f"Ошибка ввода: введите два числа ({e})")
#
# except Exception as e:
#     print(f"Произошла неизвестная ошибка: {e}")
# 11. Создай код, который ловит арифметические ошибки (ArithmeticError) в одном блоке.
# Попробуй специально сделать ошибку деления на ноль или другую арифметическую ошибку.
# try:
#     a = 20
#     b = 0
#     result = a / b
#     print(result)
# except ArithmeticError as e:
#     print(e)
    # 12. Запроси у пользователя два числа и выполни деление.
    # Если деление прошло успешно без ошибок — выведи
    # "Деление выполнено успешно" через (но не в блоке try)
# def divider():
#     try:
#         a = int(input("Первое число: "))
#         b = int(input("Второе число: "))
#         result = a / b
#
#     except (ValueError, ZeroDivisionError) as e:
#         print(f"Ошибка: {e}")
#         return None
#
#     else:
#         print("Деление выполнено успешно")
#         return result
#
#
# print(divider())
# 13. Расширь код из Задания 12:
# Добавь блок, в котором будет выводиться
# "Работа программы завершена", независимо от успеха деления.
# def divider():
#     try:
#         a = int(input("Первое число: "))
#         b = int(input("Второе число: "))
#         result = a / b
#
#     except (ValueError, ZeroDivisionError) as e:
#         print(f"Ошибка: {e}")
#         return None
#
#     else:
#         print("Деление выполнено успешно")
#         return result
#     finally:
#         print("Работа программы завершена")
#
# print(divider())
# 14. Реализуй две вложенные конструкции:
# Внешний try/except обрабатывает неверный ввод (строки вместо чисел);
# Внутренний try/except ловит деление на ноль.
# try:
#     a = int(input("Первое число: "))
#     b = int(input("Второе число: "))
#
#     try:
#         result = a / b
#         print("Результат:", result)
#     except ZeroDivisionError:
#         print("Ошибка: деление на ноль")
#
# except ValueError:
#     print("Ошибка ввода: введите числа")
# 15. Вынеси обработку деления в отдельную функцию divide(x, y)
# с собственным try/except.
# Во внешнем коде обработай только ошибку ввода.
# def divide(x, y):
#     try:
#         return x / y
#     except ZeroDivisionError:
#         print("Ошибка: деление на ноль")
#         return None
#
#
# try:
#     a = int(input("Первое число: "))
#     b = int(input("Второе число: "))
#
#     result = divide(a, b)
#     if result is not None:
#         print("Результат:", result)
#
# except ValueError:
#     print("Ошибка ввода: введите числа")


