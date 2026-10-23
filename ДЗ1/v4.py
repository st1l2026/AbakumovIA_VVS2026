
class CalculatorMoney:
    def __init__(self, check: float, discount: float, tip_percent: float, num_persons: int, value: float):
        self.check = check
        self.discount = discount
        self.tip_percent = tip_percent
        self.num_persons = num_persons
        self.value = value
        
    def calculate_1(self):
        disc_check = self.check * (100 - self.discount) / 100
        in_value = disc_check / self.value
        return in_value

    def calculate_2(self):
        disc_check = self.check * (100 - self.discount) / 100
        with_tip = disc_check * (100 + self.tip_percent) / 100
        return with_tip / self.num_persons

check = float(input("Сумма чека>>>"))
discount = float(input("Скидка (%)>>>"))

t = int(input('Какой вам нужен калькулятор? Валютный или Оплата на человека? Введите 1 или 2 соответственно для выбора>>>'))

if t == 1:
  value_course = float(input("Какой курс по отношению к рублю валюты, которой хотите заплатить>>>"))
  calc = CalculatorMoney(check, discount, 0, 0, value_course)
  print('Вы должны заплатить столько в данной валюте>>>', calc.calculate_1())
else:
  tip = float(input("Чаевые (%)>>>"))
  num_person = int(input("Количество человек>>>"))
  calc = CalculatorMoney(check, discount, tip, num_person, 0)
  print('На человека столько денег>>>', calc.calculate_2())
