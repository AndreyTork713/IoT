import time

def rasch_ustavki(dnt, graf):
    print('Расчет t-уставки...')
    time.sleep(1.5)
    for i in graf:
        if dnt == i:
           return graf[i]