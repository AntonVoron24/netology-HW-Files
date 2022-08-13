from pprint import pprint


def get_cook_book():
    with open('recipes.txt', encoding='utf-8') as f:
        # Сначала распределим на списке по структуре файла
        name = []  # Наименование блюда
        ing_count = []  # Кол-во ингредиентов в блюде
        ing_list = []  # Ингридиенты
        list1 = ['ingredient_name', 'quantity', 'measure']  # Список для создания новой структуры словаря
        for i in f:
            k = i.strip('\n')
            if k.replace('\n', ' ').isdigit():  # Проверка на числа (кол-во ингредиентов)
                ing_count += k
            elif k.replace(' ', '').replace('-', '').isalpha():  # Проверка на буквы (наименование блюда)
                name.append(k)
            else:
                if k:  # Все остальное является ингредиентоами, поэтому попадает в этот блок
                    ingredients = dict(zip(list1, k.split(' | ')))
                    ing_list.append(ingredients)
        k = 0
        d = 0
        cook_book = dict.fromkeys(name)
        for i in ing_count:
            ing = ing_list[k:k+int(i)]
            k = k + int(i)
            dish_name = name[d]
            d += 1
            cook_book[dish_name] = ing
        return cook_book


pprint(get_cook_book())


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        if dish not in get_cook_book().keys():  # Сначала проверяем есть ли Блюдо в списке
            print(f'Блюда {dish} отсутствует в поваренной книге.')
        else:
            for name in get_cook_book()[dish]:
                if name['ingredient_name'] not in shop_list:
                    shop_list[name['ingredient_name']] = {
                        'measure': name['measure'],
                        'quantity': int(name['quantity']) * person_count}
                elif name['ingredient_name'] in shop_list:  # Этот блок необходим т.к. словарь перезаписывается.
                    shop_list[name['ingredient_name']]['quantity'] += int(name['quantity']) * person_count

    return shop_list


pprint(get_shop_list_by_dishes(['Омлет', 'Омлет', 'Пицца', 'Пицца'], 4))
