import time
from mymodule_1 import rasch_ustavki

ust_Podacha = {-30: 80, -20: 70, -10: 60, 0: 50, 10: 40}
ust_Obratka = {-30: 75, -20: 65, -10: 55, 0: 45, 10: 35}

print('Введите значение наружной температуры...')
dat_NT = int(input())
time.sleep(1.5)

print('Подача: ' + str(rasch_ustavki(dat_NT, ust_Podacha)))
print('Обратка: ' + str(rasch_ustavki(dat_NT, ust_Obratka)))