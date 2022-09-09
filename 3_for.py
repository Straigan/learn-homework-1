"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

import statistics


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """

    products =  [
                    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
                    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
                    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
                ]

    products_all_sold = []

    for product in products:
        products_all_sold.append(sum(product['items_sold']))

        product = product['product']
        sum_sold_product = sum(product['items_sold'])
        avg_sold_product = round(statistics.mean(product['items_sold']))

        print(f'Товар {product}, суммарное колличество продаж для этого товара - {sum_sold_product}')
        print(f'Товар {product}, среднее колличество продаж для этого товара - {avg_sold_product}')
        print('-------')
    
    sum_sold_all_product = sum(products_all_sold)
    avg_sold_all_product = round(statistics.mean(products_all_sold))

    print(f'Cуммарное количество продаж всех товаров - {sum_sold_all_product}')
    print(f'Cреднее количество продаж всех товаров - {avg_sold_all_product}')
    
if __name__ == "__main__":
    main()
