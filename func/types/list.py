
# ! Списки
# ? Перекрутка списка
def list_rewind(list_of_val: list, rewind_val: int = 1) -> list:
    '''Прокручивает список на значение rewind_val'''
    return list_of_val[rewind_val:] + list_of_val[:rewind_val]


# ? Возвращает индекс самого большого значения в списке
def max_value_index(list_of_val: list):
    '''Возвращает индекс самого большого значения в списке'''
    j = index = 0
    for i in range(len(list_of_val)):
        if j < list_of_val[i]:
            j = list_of_val[i]
            index = i
    return index


# ? Возвращает индекс самого маленького значения в списке
def min_value_index(list_of_val: list):
    '''Возвращает индекс самого маленького значения в списке'''
    j = index = 0
    for i in range(len(list_of_val)):
        if j > list_of_val[i]:
            j = list_of_val[i]
            index = i
    return index


# ? Перевод списка в массив
def list_to_array(list_of_val: list, x: int, y: int):
    '''Перевод списка в массив'''
    answer = []
    for i in range(1, y + 1):
        ans_list = list_of_val[i * x - x:i * x]
        answer.append(ans_list)
    return answer


# ! Методы поиска
# ? Бинарный поиск совпадений
def matches_b(list_of_val: list):
    '''Бинарный поиск совпадений в списке. Возвращает да, если совпадения есть'''
    a = set(list_of_val)
    if len(a) < len(list_of_val):
        return False
    return True


# ? Полноценный поиск совпадений в списке
def matches_f(list_of_val: list):
    '''Возвращает список всех совпадений в заданном списке'''
    list_of_matches = []
    for i in list_of_val:
        if i in list_of_matches: continue
        if list_of_val.count(i) > 1: list_of_matches.append(i)
    if len(list_of_matches) > 0:
        return list_of_matches
    return False