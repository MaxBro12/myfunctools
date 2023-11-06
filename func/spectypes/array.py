
# ! Массивы
# ? Поворот матрицы
def rotate_array(m):
    '''Поворот матрицы'''
    return [[m[j][i] for j in range(len(m))] for i in range(len(m[0]) - 1, -1, -1)]


# ? Возвращает значение из массива, на основе порядкого индекса
def array_value_backer(massive, index: int):
    '''Возвращает значение из массива, на основе порядкого индекса'''
    return massive[index // 3][index % 3]


# ? Возвращает индексы из массива, на основе порядкого индекса
def array_index_backer(massive, index: int):
    '''Возвращает значение индексов, на основе порядкого индекса'''
    return index // len(massive), index % massive[0]


# ? Перевод массива в список
def array_to_list(massive) -> list:
    '''Переводит массив в список'''
    answer = []
    for i in massive:
        for j in i:
            answer.append(j)
    return answer
