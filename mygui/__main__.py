from PySide6.QtWidgets import (
    QWidget,
    QApplication,
)

from gui import PyGui


from settings import base_config


def main():
    app = QApplication([])
    widget = PyGui(base_config, None)
    widget.show()
    exit(app.exec())



if __name__ == '__main__':
    main()
