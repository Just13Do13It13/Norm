# 1. Создай класс Dog с атрибутами класса species = "canis" и legs = 4.
# Затем создай два объекта этого класса и измени у одного из них локальный атрибут.
# Проверь, как это повлияло на значения у обоих объектов.
# Убедись, что __dict__ объектов отражает изменения.
# class Dog:
#     "Класс собачек забиячек"
#     species = "canis"
#     legs = 4
#
# print(Dog.__doc__)
# Dog.legs = 3
# print(Dog.species, Dog.legs)
# print(Dog.__dict__)
# 2. Добавь в класс Dog строку документации, описывающую его назначение.
# Затем выведи её на экран.
# После этого добавь в объект класса новые атрибуты name и age,
# а затем удали name.
# Проверь, что произойдёт при попытке снова вывести объект.name.
# Dog.name = 'Щенок'
# Dog.age = 16
# print(Dog.name, Dog.age)
# del Dog.name
# print(Dog.name)
#
# 3. Создай класс User с атрибутами класса role = "guest" и active = True.
# С помощью функций getattr(), setattr(), hasattr() и delattr():
#
# измени значение role на "admin",
# проверь наличие active,
# добавь новый атрибут email,
# удали role.
# Убедись, что всё работает корректно, и выведи итоговое содержимое __dict__ класса User.
# class User:
#     role = "guest"
#     active = True
#
# setattr(User, "role", "admin")
#
# print(hasattr(User, "active"))
#
# setattr(User, "email", "userds")
#
# delattr(User, "role")
#
# print(User.__dict__)