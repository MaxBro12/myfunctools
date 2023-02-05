from typing import Union


# ? Возврат значения в пределах максимального или минимального
def clamp(
    value: Union[int, float],
    Min: Union[int, float],
    Max: Union[int, float]
) -> Union[int, float]:
    '''Возвращает значение в пределах максимального
    или минимального значения.'''
    return max(min(value, Max), Min)


# ? Возврат bool если значение в пределах max и min
def threshold(
    value: Union[int, float],
    Min: Union[int, float],
    Max: Union[int, float]
) -> bool:
    """Возврат bool если значение в пределах max и min"""
    return True if Min <= value <= Max else False
