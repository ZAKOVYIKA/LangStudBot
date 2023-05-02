from webhook.models import User
import numpy as np

# Проверяем, что запись существует в БД
def db_exists(uid = None):
    if isinstance(uid, float) | isinstance(uid, int):
        return User.objects.filter(uid = uid).exists()
    else:
        return False
    # end
# end

# Считываем внутренний номер пользователя
def db_id(uid = None):
    if uid is None:
        return None
    # end

    if User.objects.filter(uid = uid).exists():
        u = User.objects.filter(uid = uid)
        return [u[j].ctgid for j in range(len(u))]
    else:
        return None
    # end
# end

# Создаём нового пользователя
def db_create(uid = None):
    if (uid is None):
        return None
    # end

    if db_exists(uid):
        return None
    else:
        u = User(uid = uid)
        u.save()
        return u
    # end
# end

# Считываем пользователя
def db_read(uid = None):
    if (uid is None):
        return None
    # end

    if db_exists(uid):
        u = User.objects.get(uid = uid)
        return u
    else:
        return None
    # end
# end

# Удаляем пользователя
def db_delete(uid = None):
    if (uid is None):
        return None
    # end

    if db_exists(uid):
        u = User.objects.get(uid = uid)
        u.delete()
        return u
    else:
        return None
    # end
# end

# Очищаем таблицу
def db_delete_all():
    User.objects.filter().delete()
# end