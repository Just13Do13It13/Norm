# ""
# ======================================
# 1. Создай базовый класс Shape с методом area(), который возвращает 0.
# Отнаследуй два класса: Circle и Square.
# Переопредели метод area() так, чтобы он возвращал площадь круга или квадрата.
#
# c = Circle(5)
# s = Square(4)
#
# print(c.area())  # ~78.5
# print(s.area())  # 16
# ======================================
# 2. Создай базовый класс BasePage с методом open(url).
# Сделай добавь магический init, в котором указан текст на странице (любой)
# От него унаследуй LoginPage и добавь метод find(text).
# Проверь, что методы из базового класса тоже доступны:
# page = LoginPage()
# page.open("https://example.com/login")
# page.text("Зима")
# Вывод в консоли:
# На странице найден текст: "Зима"
# ======================================
# 3. Создай свой класс ResultList,
# который наследует list и добавляет метод success_count(),
# возвращающий количество успешных результатов (где item["status"] == "passed").
#
# results = ResultList([
#     {"status": "passed"},
#     {"status": "failed"},
#     {"status": "passed"},
# ])
#
# print(results.success_count())  # 2
# ======================================
# 4. Создай классы BaseStep и LoginStep, отнаследуй второй от первого.
#  Создай объект step = LoginStep()
#  Проверь, что он является экземпляром и LoginStep, и BaseStep, и object.
#
# print(issubclass(LoginStep, BaseStep))  # True
# print(isinstance(step, BaseStep))       # True
# print(isinstance(step, object))         # True
# ======================================
# 5. Создай класс ExtendedDict, который наследуется от dict,
# и переопредели __str__, чтобы словарь красиво выводился в формате:
# ключ: значение
# ключ: значение
# Пример:
# d = ExtendedDict(a=1, b=2)
# print(d)
# Ожидаемый вывод:
# a: 1
# b: 2
# ======================================
# 6. Создай два класса:
#
# Widget: принимает x, y и сохраняет как self.x, self.y;
# Button: наследует Widget, добавляет label, но обязательно вызывает super().
# Проверь, что всё сохраняется корректно.
#
# btn = Button(100, 200, "OK")
# print(btn.x, btn.y, btn.label)  # 100 200 OK
# ======================================
# 7. Модифицируй Button, чтобы не вызывать super() вовсе.
# Что произойдёт? Проверь через print(btn.__dict__).
# ======================================
# 8. Создай классы:
# Logger — метод log(self, msg) просто печатает сообщение;
# HTMLLogger(Logger) — переопредели метод log.
# logger = HTMLLogger()
# logger.log("Login successful")
#
# Ожидаемый вывод (обрати внимание что выводится 2 строки:
# одна из log класса Logger, другая из log класса HTMLLogger):
# [LOG] Login successful
# <p>Login successful</p>
# """