from typing import Union


def base_progress(c_val: Union[int, float] = 0, max_val: Union[int, float] = 1, prog_len: int = 1, prog_simb: str = '#', returnstr: bool = False) -> Union[str, None]:
    '''
    Отправляем в консоль готовый формат строки прогресса.
    
    Parameters:
    -----------
    - c_val (int | float) - текущее значение прогресса
    - max_val (int | float) - максимальное значение прогресса
    - prog_len (int) - символьная длинна строки
    - prog_simb (str) - символ прогресса
    - returnstr (bool) - вернуть строку (True) или сразу вывести в консоль (False)
    '''
    proc = c_val / max_val
    lprog = int(prog_len * proc)
    rprog = prog_len - lprog
    lsim = prog_simb * lprog
    rsim = '-' * rprog
    # print(f'proc: {proc}\nlp {lprog}\nrp {rprog}\nls {lsim}\nrs {rsim}')
    rstr = str(f'[{lsim}{rsim}]')

    if returnstr:
        return rstr
    else:
        print(rstr)
    return None
