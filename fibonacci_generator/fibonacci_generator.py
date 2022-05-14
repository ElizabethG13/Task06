"""
Написать генератор fibonacci, которая принимает номер значения num_count
из чисел Фибоначчи и выводит на экран результат до заданного значения.
Номер значения нужно проверить
Пример:
fibonacci(0) -> raise ValueError('Введите значение больше 1')
fibonacci(5)
1
2
3
5
8
Traceback (most recent call last):
File «C:/Python/Python3/python_generator.py», line 29, in
print(next(fib))
StopIteration
"""
iteration = int(input("Введите кол-во итераций: "))

fib1, fib2 = 0, 1
count = 0

if iteration <= 0:
   print("Введите число >0")
else:
   print("Последвоательность фибоначи:")
   while count < iteration:
       print(fib1)
       next_fib = fib1 + fib2
       fib1, fib2 = fib2, next_fib
       count += 1
