# MYPYMULTITHREAD

Базовый модуль работы с мультипоточностью в python.

Сейчас реализованно лишь работа с модулем threading.

Пример:

```python
from func.mypymultithread import MyThread


def test_list_multiply(val: list):
    """Функция перебора списка"""
    lst = [_ for _ in range(val[0])]
    for i in range(len(lst)):
        lst[i] = 10 * lst[i]
    print(f'END: {val}')


a = MyThread(test_list_multiply, (100_000_000,))
b = MyThread(test_list_multiply, (10_000_000,))
c = MyThread(test_list_multiply, (1_000_000,))


a.start()
b.start()
c.start()

a.join()
b.join()
c.join()
```

Если мы не используем мультипоточность:

```zsh
python3.11 test.py
END: (100000000,)
END: (10000000,)
END: (1000000,)
```

Если мы используем мультипочность:

```zsh
python3.11 test.py
END: (1000000,)
END: (10000000,)
END: (100000000,)
```
