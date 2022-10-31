from typing import Union


# ? Возврат значения в пределах максимального или минимального
def clamp(value, Min, Max) -> Union[int, float]:
    '''Возвращает значение в пределах максимального или минимального значения.'''
    return max(min(value, Max), Min)
