#Конвертер валют с фиксированным курсом
def convert_currency(amount, rate):
  """Конвертирует сумму по заданному курсу."""
  return amount * rate

def main():
  # Предположим, что мы конвертируем из долларов в евро.
  # Введите актуальный курс конвертации из долларов в евро.
  usd_to_eur_rate = float(input("Введите курс конвертации из USD в EUR: "))

  usd_amount = float(input("Введите сумму в USD, которую хотите конвертировать: "))

  eur_amount = convert_currency(usd_amount, usd_to_eur_rate)

  print(f"{usd_amount} USD равны {eur_amount:.2f} EUR по курсу {usd_to_eur_rate}.")

#Запускаем конвертор валют
main()
