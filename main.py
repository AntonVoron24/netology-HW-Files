from pprint import pprint
from collections import Counter


def get_cook_book():
    with open('recipes.txt', encoding='utf-8') as f:

        ing_count = []
        name = []
        ing_list = []
        list1 = ['ingredient_name', 'quantity', 'measure']
        for i in f:
            k = i.strip('\n')
            if k.replace('\n', ' ').isdigit():
                ing_count += k
            elif k.replace(' ', '').replace('-', '').isalpha():
                name.append(k)
            else:
                if k:
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
    dish_count = Counter(dishes)
    for name, count in dish_count.items():
        if name not in get_cook_book().keys():
            print(f'Блюда {name} нет в поваренной книге')
        else:
            for i, v in get_cook_book().items():
                for k in v:
                    if i == name:
                        shop_list[k['ingredient_name']] = {
                            'measure': k['measure'],
                            'quantity': int(k['quantity']) * person_count * count}
    return shop_list


pprint(get_shop_list_by_dishes(['Омлет', 'Пицца'], 3))
