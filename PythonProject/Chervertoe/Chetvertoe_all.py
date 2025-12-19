# 1. Создай класс SecureData, который:
#
# имеет атрибут __secret, задаваемый в __init__;
# переопределяет __getattribute__, чтобы при попытке получить __secret извне выбрасывать ValueError;
# внутри класса доступ к __secret должен работать.
# Проверь:
# data = SecureData("пароль123")
# print(data.__secret)      # ошибка
# print(data.get_secret())  # "пароль123"
# class SecureData:
#     def __init__(self, secret):
#         self.__secret = secret
#
#     def __getattribute__(self, name):
#         if name == "_SecureData__secret":
#             raise ValueError("Доступ запрещён")
#         return super().__getattribute__(name)
#
#     def get_secret(self):
#         return self.__secret
#
#     def __setattr__(selfs, name, value):
#         if name == "token":
#             raise ValueError("Нельзя нах с таким именем АЁ")
#         super().__setattr__(name, value)
#
# data = SecureData("пароль123")
# data.token = "abc123"  # ❌ AttributeError
# data.other = "ok"      # ✅ работает
# print(data.__secret)      # здесь будет ошибка
# print(data.get_secret())    # работает: "пароль123"
# 3. Создай класс SafeDict, в котором:
#
# нет атрибута default;
# реализован __getattr__, который возвращает "N/A" (это строка) при попытке получить несуществующий атрибут;
# реализован __delattr__, который пишет "Удалён атрибут <имя>" и действительно удаляет атрибут.
# Проверь:
# d = SafeDict()
# print(d.unknown)     # "N/A"
# d.key = 10
# del d.key            # "Удалён атрибут key"
# class SafeDict(dict):
#     def __getattr__(self, name):
#         return "N/A"
#
#     def __delattr__(self, item):
#         print(f"Удалён атрибут {item}")
#         super().__delattr__(item)
#
# d = SafeDict()
# print(d.unknown)
# d.key = 10
# print(d.key)
# 4. Создай класс Employee с приватными полями __name и __salary.
# Добавь @property для поля salary, а также сеттер с валидацией:
#
# зарплата должна быть положительным числом;
# если нет — выбрасывать ValueError.
# Проверь, что:
# e = Employee("Daniil", 5000)
# print(e.salary)   # 5000
# e.salary = 8000
# print(e.salary)   # 8000
# e.salary = -100   # ❌ ValueError
# class Employee(object):
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#
#     @property
#     def salary(self):
#         return self.__salary
#
#     @salary.setter
#     def salary(self, value):
#         if value <= 0:
#             raise ValueError("Зарплата должна быть положительным числом")
#         self.__salary = value
#
#     @salary.deleter
#     def salary(self):
#         print("зарплата удалена")
#         del self.__salary
#
# e = Employee("Daniil", 5000)
# print(e.salary)     # 5000
#
# e.salary = 8000
# print(e.salary)     # 8000
#
# e.salary = -100     # ❌ ValueError
# del e.salary
# print(e.__dict__)  # salary нет
# 5. Добавь @deleter для поля salary, чтобы при удалении выводилось "зарплата удалена"
# и поле реально исчезало.
# Проверь:
#
# del e.salary
# print(e.__dict__)  # salary нет
# 6. Представь, что ты пишешь обёртку над HTML-формой.
# Создай класс LoginForm с полем username, которое реализовано через @property.
#
# Логика:
# геттер возвращает self._username
# сеттер добавляет лог "username изменён"
# Проверь, что:
# form = LoginForm()
# form.username = "admin"  # выводит лог
# print(form.username)     # "admin"
# class LoginForm:
#     def __init__(self):
#         self._username = None
#
#     @property
#     def username(self):
#         return self._username
#
#     @username.setter
#     def username(self, value):
#         print("username изменён")
#         self._username = value
#
# form = LoginForm()
# form.username = "admin"  # выводит лог
# print(form.username)     # "admin"
# 7. Создай класс Card, где:
# поле __number хранит номер карты (строка);
# в @property возвращай номер с маской **** **** **** 1234;
# в @setter проверяй, что номер состоит из 16 цифр;
# в @deleter логируй удаление номера с текущим временем.
# Напиши тесты (через assert)
# проверку установки корректного номера;
# проверку исключения при вводе короткого номера;
# проверку вывода замаскированного номера.
# from datetime import datetime
#
# class Card:
#     def __init__(self, number: str):
#         self.num = number
#
#     @property
#     def num(self):
#         """Возвращает замаскированный номер"""
#         # последние 4 цифры
#         last4 = self.__number[-4:]
#         return f"**** **** **** {last4}"
#
#     @num.setter
#     def num(self, value: str):
#         """Проверяет, что передан номер из 16 цифр"""
#         if not (isinstance(value, str) and value.isdigit() and len(value) == 16):
#             raise ValueError("Номер карты должен быть строкой из 16 цифр")
#         self.__number = value
#
#     @num.deleter
#     def num(self):
#         print("Номер карты удалён:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#         del self.__number
#
# # 1 — корректная установка номера
# c = Card("1234567812345678")
# assert c.num == "**** **** **** 5678"
#
# # 2 — проверка исключения при коротком номере
# try:
#     c.num = "123"
#     assert False  # сюда попасть не должны
# except ValueError:
#     pass  # всё правильно
#
# # 3 — проверка маски
# c.num = "9999888877776666"
# assert c.num == "**** **** **** 6666"
#
# print("Все тесты пройдены!")
# 8. Создай класс UserData для API регистрации пользователя:
# email — строка, содержит @;
# age — целое число ≥ 18;
# is_active — bool;
# свойство .json возвращает словарь для запроса.
# Напиши тест (через assert)
# проверь, что при age = 15 выбрасывается ValueError;
# проверь, что email без @ вызывает ошибку;
# проверь, что json возвращает корректную структуру.
# class UserData:
#     def __init__(self, email: str, age: int, is_active: bool):
#         if '@' not in email:
#             raise ValueError("Email должен содержать '@'")
#         if age < 18:
#             raise ValueError("Возраст должен быть ≥ 18")
#         if not isinstance(is_active, bool):
#             raise ValueError("is_active должен быть булевым значением")
#         self.email = email
#         self.age = age
#         self.is_active = is_active
#
#     @property
#     def json(self):
#         return {
#             "email": self.email,
#             "age": self.age,
#             "is_active": self.is_active
#         }
#
#
# # 1. Проверка ValueError для age < 18
# try:
#     UserData("test@example.com", 15, True)
# except ValueError as e:
#     assert str(e) == "Возраст должен быть ≥ 18"
#
# # 2. Проверка ValueError для email без '@'
# try:
#     UserData("testexample.com", 20, True)
# except ValueError as e:
#     assert str(e) == "Email должен содержать '@'"
#
# # 3. Проверка корректного .json
# user = UserData("test@example.com", 25, True)
# assert user.json == {"email": "test@example.com", "age": 25, "is_active": True}
#
# print("Все тесты прошли")