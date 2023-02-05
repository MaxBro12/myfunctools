from typing import Union


def base_progress(
    c_val: Union[int, float] = 0,
    max_val: Union[int, float] = 1,
    prog_len: int = 1,
    returnstr: bool = False
):
    '''
    Отправляем в консоль готовый формат строки прогресса.
    Parameters:
    -----------
    - c_val (int | float) - текущее значение прогресса
    - max_val (int | float) - максимальное значение прогресса
    - prog_len (int) - символьная длинна строки
    - returnstr (bool) - вернуть строку или сразу вывести в консоль
    '''
    proc = c_val / max_val
    lprog = int(prog_len * proc)
    rprog = prog_len - lprog
    lsim = '◼' * lprog
    rsim = '-' * rprog
    # print(f'proc: {proc}\nlp {lprog}\nrp {rprog}\nls {lsim}\nrs {rsim}')
    rstr = str(f'[{lsim}{rsim}]')

    if returnstr:
        return rstr
    else:
        print(rstr)
