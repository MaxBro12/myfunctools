from typing import TypedDict, Literal


class AppConfig(TypedDict):
    width: int
    height: int
    opacity: int

    title: str
    way_to_icon: str
