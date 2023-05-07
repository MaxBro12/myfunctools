from typing import TypedDict, Literal


class AppConfig(TypedDict):
    width: int
    height: int
    opacity: int | float

    title: str
    way_to_icon: str


class MenuBarConfig(TypedDict):
    show_title_icon: bool
    show_title_name: bool
