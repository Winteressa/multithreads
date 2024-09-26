from threading import Thread, Lock
from time import sleep
from random import randint

counter = 0
summ = 0
average = 0

def rnd(rnd_numbers, lock):
    global counter
    rnd_numbers = []
    lock.acquire()
    rnd_numbers = counter
    rnd_numbers = [randint(0, 100) for i in range(10)]

    sleep(0.1)

    counter = rnd_numbers
    lock.release()


def summa(summ, lock):
    global summ
    lock.acquire()
    summ = sum(rnd_numbers)

    sleep(0.1)

    lock.release()

def avg(average, lock):
    global average
    lock.acquire()
    average = sum(rnd_numbers) / len(rnd_numbers)

    sleep(0.1)

    lock.release()

    three_thread = ThreeThread()

t1 = Thread(target=three_thread.rnd())
t2 = Thread(target=three_thread.summ())
t3 = Thread(target=three_thread.avg())

t1.start()
t1.join()

t2.start()
t3.start()

t2.join()
t3.join()

print(*three_thread.rnd_numbers, sep=', ')
print(f'Сумма {three_thread.summa}')
print(f'Среднее арифметическое {three_thread.average}')