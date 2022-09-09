"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def get_string(str_1, str_2):
    """
    Проверка строки в первом аргументе со строкой во втором аргументе
    """
    if type(str_1) != str or type(str_2) != str:
        return 0
    elif str_1 == str_2:
        return 1
    elif str_2 == 'learn':
        return 3
    elif len(str_1) > len(str_2):
        return 2
    


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    comparison_str1 = get_string(1212, 'булочка')
    print(comparison_str1)

    comparison_str2 = get_string('булочка', 1212)
    print(comparison_str2)

    comparison_str3 = get_string('булочка', 'булочка')
    print(comparison_str3)

    comparison_str4 = get_string('булочкаааа', 'булочка')
    print(comparison_str4)

    comparison_str5 = get_string('булочка', 'learn')
    print(comparison_str5)


if __name__ == "__main__":
    main()
