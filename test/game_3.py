import random


print("загадайте число от 0 до 100")
print(
    "Если мое число меньше или больше вашего вводите '<' или '>' соответственно, а если я угадал, то введите 'y' и нажмите Enter"
)
rnd = 50
min_diapazona = 0
max_diapazona = 100
otvet = ""
while 1 > 0:
    print("Мое число:", rnd, "я угадал? Диапазон от", min_diapazona, "до",
          max_diapazona)
    otvet = input()
    if otvet == "y":
        print("Я угадал! Игра окончена.")
        break
    elif otvet == "<":
        max_diapazona = rnd - 1
        try:
            rnd = random.randint(min_diapazona, max_diapazona)
        except:
            print("Вы мухлевщик! Я с вами больше не играю! Игра окончена!")
    elif otvet == ">":
        min_diapazona = rnd + 1
        try:
            rnd = random.randint(min_diapazona, max_diapazona)
        except:
            print("Вы мухлевщик! Я с вами больше не играю! Игра окончена!")
            break
    else:
        print("Неправельнй ввод! Допустимые символы: '<', '>' и 'y'")