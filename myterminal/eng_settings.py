from os import get_terminal_size


# * Да / нет значения
confirmation = ('Y', 'y', 'Д', 'д')
rejection = ('n', 'н')


# * Базовое положение конфига
config_loc = 'config.toml'

# * Конфиг
conf_separator = '=' * get_terminal_size()[0]
