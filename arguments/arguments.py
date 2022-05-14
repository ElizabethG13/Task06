"""
Написать функцию dict_from_args, которая принимает неограниченное
количество позиционных аргументов и неограниченное количество аргументов
ключевых-слов.
Если все позиционные аргументы - целые числа, то рассчитать их сумму. Если
нет, то кинуть ошибку TypeError("Все позиционные аргументы должны быть целыми").
Проверить, что все аргументы целые можно с помощью функции all:
https://pyneng.readthedocs.io/ru/latest/book/10_useful_functions/all_any.html
Если все аргументы - ключевые слова являются строками, то найти максимальную
длину слова. Если нет, то кинуть ошибку TypeError("Все аргументы - ключевые
слова должны быть строками").
Функция должна вернуть словарь, вида:
{
    "args_sum": 13,
    "kwargs_max_len": 7
}
"""


def isint(num):
    try:
        temp = str(num)
        int(temp)
        return True
    except TypeError:
        # print("Все аргументы - ключевые слова должны быть строками ")
        return False



def dict_from_args (*args, **kwargs):
    rezult = 0
    if (all(type(num) == type(5) for num in args)):
        for num in args:
            rezult += num
        # print(rezult)
    else:
            TypeError
            print("Все позиционные аргументы должны быть целыми.")
            rezult = "-"


    len_word = 0
    if (all(type(word) == type('stroka') for word in kwargs)):
        for key, word in kwargs.items():
            temp_word_len = len(word)
            if len_word < temp_word_len:
                len_word = temp_word_len
        # print(temp_word_len)
    else:
            TypeError
            print("Все аргументы - ключевые слова должны быть строками.")
            len_word = "-"

    d = {'args_sum': rezult, 'kwargs_max_len': len_word}
    print(d)


dict_from_args(5, 6, 7, firts="")
dict_from_args(5, 6, 7.3, first="cat", mid="cats")
dict_from_args(5, 6, 7, 8, 9, 10, first="cats", mid="cat")
dict_from_args(5, first="cat", mid="cats")
dict_from_args(5, first="", mid="cats and dogs")

"""Не смогла проверить на наличие не строки в wargs
dict_from_args(5, first="cat", mid="cats12346", last=5)
"""