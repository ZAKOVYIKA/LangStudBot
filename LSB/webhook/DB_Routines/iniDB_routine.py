import os
from pathlib import Path
import numpy as np

def iniDB(txtname = '', valout = None):
    '''
    Используется для считывания файлов с начальными записями для БД.
    Файлы заполнены по специальному формату.
    ~ - начало нового блока данных (новой записи)
    # - начало нового элемента записи

    На вход:
        txtname - название файла с БД с расширением .txt
        valout - число элементов для одной записи
    '''

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    # Путь до папки с .txt файлами БД
    txtpath = os.path.join(BASE_DIR, 'iniDBtxt')

    # Файл для считывания
    txtDB = os.path.join(txtpath, txtname)
    print(txtDB)
    # Проверим, что такой файл вообще есть
    if not(os.path.isfile(txtDB)):
        raise ValueError('Введено некорректное имя файла или файла не существует!')
    # end


    # Проверим, что число полей ввобще введно
    if (valout is None):
        raise ValueError('Введи число элементов!')
    elif (not(isinstance(valout, float))) & (not(isinstance(valout, int))):
        raise ValueError('Введи именно число!')
    elif (valout <= 0):
        raise ValueError('Введи корректное число!')
    # end

    # Создадим костыль массива для ответа
    out = np.empty(shape = (0, valout), dtype = object)

    # Начнём считывание
    with open(txtDB, mode = 'r',encoding =  'UTF-8') as file:
        data = file.readlines()
        numlines = len(data)

        # Число блоков данных
        block = 0
        for k in range(numlines):
            # Выбранная строка текста
            line = data[k]

            # Если содержит ~, значит начало новго блока данных
            if '~' in line:
                block = block + 1
                block_elems = 0
                # Если уже считали хоть один блок, то надо его записать
                if block > 1:
                    out = np.append(out, tout, axis = 0)
                # end

                # Создаём временную строку для записи считанных данных
                tout = np.empty(shape=(1, valout), dtype=object)

            # Если содержит #, значит начало новго элемента блока
            elif '#' in line:
                block_elems = block_elems + 1
                tout[0, block_elems - 1] = ''

            # Если выполняем этот кусочек, то уже идёт запись текста в ответ
            else:
                tout[0, block_elems-1] = tout[0, block_elems-1] + line
            # end
        # end
        # И записать последний блок
        out = np.append(out, tout, axis=0)

    # end
    return out
# end
