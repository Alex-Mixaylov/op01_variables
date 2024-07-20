#Создать калькулятор — программу, в которой мы вводим 2 числа, и с ними производятся сразу все математические действия, рассмотренные в уроке.
def perform_operations(a, b):
  print(f"Сложение: {a} + {b} = {a + b}")
  print(f"Вычитание: {a} - {b} = {a - b}")
  print(f"Умножение: {a} * {b} = {a * b}")
  print(f"Деление: {a} / {b} = {a / b}")
  print(f"Целая часть от деления: {a} // {b} = {a // b}")
  print(f"Остаток от деления: {a} % {b} = {a % b}")
  print(f"Возведение в степень: {a} ** {b} = {a ** b}")

def main():
  try:
      # Запрашиваем у пользователя два числа
      number1 = float(input("Введите первое число: "))
      number2 = float(input("Введите второе число: "))

      # Выполняем операции
      perform_operations(number1, number2)
  except ValueError:
      print("Пожалуйста, введите корректные числа.")
  except ZeroDivisionError:
      print("Ошибка: Деление на ноль невозможно.")
      
#Вызов основной функции
main()