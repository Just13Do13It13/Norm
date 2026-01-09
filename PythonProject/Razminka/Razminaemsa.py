# def calculate_total(price, discount_type):
#     if discount_type == "none":
#         return price
#     elif discount_type == "seasonal":
#         return price * 0.9
#     elif discount_type == "vip":
#         return price * 0.8
#     elif discount_type == "black_friday":
#         return price * 0.5
#     else:
#         raise ValueError("unknown discount type")




# def no_discount(price):
#     return price
#
# def discount_seasonal(price):
#     return price * 0.9
#
# def discount_vip(price):
#     return price * 0.8
#
# def discount_black_friday(price):
#     return price * 0.5
#
#
# DISCOUNTS = {
#     "none": no_discount,
#     "seasonal": discount_seasonal,
#     "vip": discount_vip,
#     "black_friday": discount_black_friday
# }
#
# def calculate_total(price, discount_type):
#     try:
#         dis = DISCOUNTS[discount_type]
#     except KeyError:
#         raise Exception("unknown discount type")
#
#     return dis(price)
#
# DISCOUNTS["new_year"] = lambda price: price * 0.7
# DISCOUNTS["Sanya"] = lambda price: price * 0
#
# print(calculate_total(100, "none"))
# print(calculate_total(100, "vip"))
# print(calculate_total(100, "seasonal"))
# print(calculate_total(100, "black_friday"))
# print(calculate_total(100, "new_year"))
# print(calculate_total(100, "Sanya"))
# def func():
#     a = 3
#
#     def inner(b):
#         return a+b
#
#     return inner
#
# inner = func()
# print(inner(5))
# print(inner(7))