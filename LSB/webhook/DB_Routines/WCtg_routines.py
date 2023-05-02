from webhook.models import WCategory
import webhook.DB_Routines.WCtg_routines as WCr
import numpy as np

# Проверяем, что запись существует в БД
def db_exists(value = None, uid = None):
    if isinstance(value, float) | isinstance(value, int):
        return WCategory.objects.filter(ctgid = value, ctg_uid = uid).exists()
    elif isinstance(value, str):
        return WCategory.objects.filter(Name = value, ctg_uid = uid).exists()
    else:
        return False
    # end
# end

# Считываем внутренний номер категории
def db_id(name = None, uid = None):
    if (name is None) | (uid is None):
        return None
    # end

    if WCategory.objects.filter(Name = name, ctg_uid = uid).exists():
        ctg = WCategory.objects.filter(Name = name, ctg_uid = uid)
        return [ctg[j].ctgid for j in range(len(ctg))]
    else:
        return None
    # end
# end

# Создаём новую категорию
def db_create(name = None, uid = None):
    if (name is None) | (uid is None):
        return None
    # end

    if db_exists(name, uid):
        return None
    else:
        ctg = WCategory(Name = name, ctg_uid = uid)
        ctg.save()
        return ctg
    # end
# end

# Считываем все категории по uid
def db_read_uid(uid = None):
    if (uid is None):
        return None
    # end

    if WCategory.objects.filter(ctg_uid = uid).exists():
        ctg = WCategory.objects.filter(ctg_uid = uid)
        return ctg
    else:
        return None
    # end
# end

# Считываем категорию по id
def db_read_dbid(dbid = None, uid = None):
    if (dbid is None) | (uid is None):
        return None
    # end

    if WCategory.objects.filter(ctgid = dbid, ctg_uid = uid).exists():
        ctg = WCategory.objects.filter(ctgid = dbid, ctg_uid = uid)
        return ctg
    else:
        return None
    # end
# end

# Считываем категорию по имени
def db_read_name(name = None, uid = None):
    if (name is None) | (uid is None):
        return None
    # end

    if WCategory.objects.filter(Name = name, ctg_uid = uid).exists():
        ctg = WCategory.objects.filter(Name = name, ctg_uid = uid)
        return ctg
    else:
        return None
    # end
# end

# Ищем категорию по имени
def db_search_name(name = None, uid = None):
    if (name is None) | (uid is None):
        return None
    # end
    print(name)
    if WCategory.objects.filter(Name__contains = name, ctg_uid = uid).exists():
        ctg = WCategory.objects.filter(Name__contains = name, ctg_uid = uid)
        return ctg
    else:
        return None
    # end
# end

# Обновляем категорию
def db_update(ctgid = None, new_name = '', uid = None):
    if (ctgid is None) | (uid is None) | (ctgid == 1):
        return None
    # end

    if db_exists(ctgid, uid):
        ctg = WCategory.objects.get(ctgid=ctgid, ctg_uid = uid)
        ctg.Name = new_name
        ctg.save()
        return ctg
    else:
        return None
    # end
# end

# Удаляем категорию
def db_delete(ctgid = None, uid = None):
    if (ctgid is None) | (uid is None) | (ctgid == 1):
        return None
    # end

    if db_exists(ctgid, uid):
        ctg = WCategory.objects.get(ctgid=ctgid, ctg_uid = uid)
        ctg.delete()
        return ctgid
    else:
        return None
    # end
# end

# Очищаем таблицу
def db_delete_all(uid = None):
    if uid is None:
        return None
    # end

    WCategory.objects.filter(ctg_uid = uid).delete()
# end