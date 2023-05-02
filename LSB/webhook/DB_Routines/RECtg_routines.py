from webhook.models import RECategory
import numpy as np

# Проверяем, что запись существует в БД
def db_exists(value = None):
    if isinstance(value, float) | isinstance(value, int):
        return RECategory.objects.filter(ctgid = value).exists()
    elif isinstance(value, str):
        return RECategory.objects.filter(Name = value).exists()
    else:
        return False
    # end
# end

# Считываем внутренний номер категории
def db_id(name = None):
    if name is None:
        return None
    # end

    if RECategory.objects.filter(Name = name).exists():
        ctg = RECategory.objects.filter(Name = name)
        return [ctg[j].ctgid for j in range(len(ctg))]
    else:
        return None
    # end
# end

# Создаём новую категорию
def db_create(name = None):
    if name is None:
        return None
    # end

    if db_exists(name):
        return None
    else:
        ctg = RECategory(Name = name)
        ctg.save()
        return ctg
    # end
# end

# Считываем категорию по имени
def db_read(name = None):
    if name is None:
        return None
    # end

    if RECategory.objects.filter(Name = name).exists():
        ctg = RECategory.objects.filter(Name = name)
        return ctg
    else:
        return None
    # end
# end

def db_name_search(strinname = None):
    if strinname is None:
        return None
    # end

    if RECategory.objects.filter(Name__contains = strinname).exists():
        ctg = RECategory.objects.filter(Name__contains = strinname)
        return ctg
    else:
        return None
    # end
# end

# Обновляем категорию
def db_update(ctgid = None, new_name = ''):
    if ctgid is None:
        return None
    # end

    if db_exists(ctgid):
        ctg = RECategory.objects.get(ctgid=ctgid)
        ctg.Name = new_name
        ctg.save()
        return ctg
    else:
        return None
    # end
# end

# Удаляем категорию
def db_delete(ctgid = None):
    if ctgid is None:
        return None
    # end

    if db_exists(ctgid):
        ctg = RECategory.objects.get(ctgid=ctgid)
        ctg.delete()
        return ctgid
    else:
        return None
    # end
# end

# Очищаем таблицу
def db_delete_all():
    RECategory.objects.all().delete()
# end

# Инициализируем таблицу категорий, считывая файл заданного формата
def db_initialize(DBinidata):
    catg_ans = []
    for k in range(DBinidata.shape[0]):
        name = DBinidata[k].replace('\n', '')
        db_create(name = name)
        catg_ans.append(db_read(name)[0])
    # end
    print(catg_ans)
    return catg_ans
#end