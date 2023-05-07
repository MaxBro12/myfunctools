from PySide6.QtWidgets import (
    QWidget,
    QApplication,
)

from gui import PyGui



def main():
    app = QApplication([])
    widget = PyGui('test', None)
    widget.show()
    exit(app.exec())



if __name__ == '__main__':
    main()
