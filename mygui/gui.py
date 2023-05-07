from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,

    QGridLayout,
    QSizeGrip,

)
from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QPalette, QColor


from settings import (
    AppConfig,
)


# Для теста
from typing import Literal
color_typed = Literal['red', 'blue', 'green']
class Color(QWidget):
    def __init__(self, color: color_typed, size: QSize | None = None):
        super(Color, self).__init__()
        self.setAutoFillBackground(True)

        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Window, QColor(color))
        self.setPalette(palette)

        if size is not None:
            self.setFixedSize(size)


class PyGui(QWidget):
    def __init__(self, config: AppConfig, inner_widget: QWidget | None) -> None:
        super().__init__()

        # ! Вырубаем заголовок
        # self.setWindowFlags(Qt.CustomizeWindowHint)
        self.setWindowFlags(Qt.FramelessWindowHint)

        self.resize(QSize(400, 400))

        self.widget = inner_widget

        self.test = Color('red', QSize(5, 5))
