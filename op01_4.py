def calculate_area(length, width):
  """Функция для вычисления площади прямоугольника."""
  return length * width

def main():
  # Запрашиваем у пользователя длину и ширину прямоугольника
  length = float(input("Введите длину прямоугольника: "))
  width = float(input("Введите ширину прямоугольника: "))

  # Вычисляем площадь
  area = calculate_area(length, width)

  # Выводим результат
  print(f"Площадь прямоугольника: {area}")

#Запуск программы
main()

