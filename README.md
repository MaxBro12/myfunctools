# MYFUNCTOOLS v1

**RU**
MyFunctools - это сборка всех моих полезных функций, методов и классов для ускорения разработки проектов.
В этом проекте вы найдете:
**ENG**
MyFunctools is a collection of all my useful functions, methods and classes to speed up project development.
In this project you will find:

## FUNC

---
В пакет входят такие модули как / The package includes modules such as:

- **DIR** - работа с файлами, их создание и обработка / working with files, their creation and processing
- **MyConsoleStyle** - пакет для кастомизации консоли / console customization package
- **myos** - пакет для обработки операционных систем / operating system processing package
- **MyTypes** - пакет с дополнительными методами, типами, классами / package with additional methods, types, classes
- **tomlpack** - работа с toml-файлами / working with toml files
- **debug** - модуль содержащий функцию для логирования / module containing a function for logging
- **myexcept** - модуль для работы своих собственных исключений / module for running your own exceptions
- **sockets** - модуль для работы с серверами / server module

## MYTERMINAL

---
Пакет способный удобно обрабатывать пользовательский ввод.
A package capable of conveniently handling user input.
Поддерживается / Supported:

- Несколько языков / Several languages
- TOML-конфиги / TOML configs
- Удобное консольное управление /  Convenient console management
- Отличная расширяемость проекта / excellent project extensibility

Для стабильной работы рекомендую создать дочерний класс. Полная инструкция в **doc**.
For stable operation, I recommend creating a child class. Full instructions in **doc**.
Пример / Example:

```python
class Program(UserInp):
    def __init__(self, config: dict = ..., args: list = None):
        super().__init__(config, args)
        self.adt_commands = {
            'hello': self.hello,
        }
        self.commands.update(self.adt_commands)

        # ! Start by one command
        if args is not None:
            self.run_only_arg(args)
```

## STARTPROJECT

---
Мой шаблон проектов. Для работы нужно лишь указать куда развернуть проект.
My project template. To work, you just need to specify where to deploy the project.
Пример / Example:

```cmd
python startproject G:\code\new_project
```

Так же автоматически подключается git репозиторий.
The git repository is also automatically connected.
