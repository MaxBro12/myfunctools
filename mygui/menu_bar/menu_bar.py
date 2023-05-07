from PySide6.QtWidgets import (
    QWidget,

    QHBoxLayout,
)
from ..spec_types import (
    MenuBarConfig,
)


class MenuBar(QWidget):
    def __int__(self, parent, config: MenuBarConfig):
        super().__init__(parent=parent)
        self.slots: list[QWidget] = []
        self.main_l = QHBoxLayout()
        self.main_l.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.main_l)
