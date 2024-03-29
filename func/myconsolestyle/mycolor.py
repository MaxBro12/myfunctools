from typing import Union


colors_front = {
    'Чёрный': 30,
    'Красный': 31,
    'Зелёный': 32,
    'Жёлтый': 33,
    'Синий': 34,
    'Фиолетовый': 35,
    'Бирюзовый': 36,
    'Белый': 37
    }

colors_bgr = {
    'Чёрный': 40,
    'Красный': 41,
    'Зелёный': 42,
    'Жёлтый': 43,
    'Синий': 44,
    'Фиолетовый': 45,
    'Бирюзовый': 46,
    'Белый': 47
    }

style_mods = {
    'Чистый': 0,
    'Жирный': 1,
    'Блеклый': 2,
    'Курсив': 3,
    'Подчёркнутый': 4,
    'Мигание': 5,
    'Зачёркнутый': 9
}

adt_style = {
    'RGB цвет': 38,
    'Двойное подчёркивание': 21,
    'Обрамлённый': 51,
    'Окружённый': 52,
    'Надчёркнутый': 53
}


def setst(
    text: str,
    style: Union[tuple, list, int] = (37),
    clear: bool = True
) -> str:
    '''Параметры:
    ----------
    - text  - любая строка
    - style - int значения стилей, которые необходимо применить к тексту.
            Можно вписать int (просто число), list или tuple
    - clear - очистить от изменений последующий текст?'''
    rtext = ''
    if isinstance(style, Union[tuple, list]):
        for i in style:
            rtext += f'\033[{i}m'
    else:
        rtext += f'\033[{style}m'
    rtext += text
    if clear:
        rtext += '\033[0m'
    return rtext
