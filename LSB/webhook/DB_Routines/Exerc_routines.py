from webhook.models import Exercise
from webhook.models import RECategory
import numpy as np
from webhook.DB_Routines import iniDB_routine
import webhook.DB_Routines.RECtg_routines as RECr

# Проверяем, что запись существует в БД
def db_exists(value = None):
    if isinstance(value, float) | isinstance(value, int):
        return Exercise.objects.filter(exercid = value).exists()
    elif isinstance(value, str):
        return Exercise.objects.filter(Name = value).exists()
    else:
        return False
    # end
# end

# Считываем внутренний номер упражнения
def db_id(name = None):
    if name is None:
        return None
    # end

    if Exercise.objects.filter(Name = name).exists():
        exerc = Exercise.objects.filter(Name = name)
        return [exerc[j].exercid for j in range(len(exerc))]
    else:
        return None
    # end
# end

# Создаём новое упражнение
def db_create(name = None, task = '', content = '', answer = '', catg = None):
    if (name is None) | (catg is None):
        return None
    # end

    if db_exists(name):
        return None
    else:
        exerc = Exercise(Name = name, Task = task, Content = content, Answer = answer, Catg = catg)
        exerc.save()
        return exerc
    # end
# end

# Считываем упражнение по номеру
def db_read(exercid = None):
    if exercid is None:
        return None
    # end

    if db_exists(exercid):
        exerc = Exercise.objects.get(exercid=exercid)
        return exerc
    else:
        return None
    # end
# end

# Считываем упражнение по категории
def db_read_catg(exerccatg = None):
    if exerccatg is None:
        return None
    # end

    if Exercise.objects.filter(Catg = exerccatg).exists():
        exerc = Exercise.objects.filter(Catg = exerccatg)
        return exerc
    else:
        return None
    # end
# end

# Считываем упражнение по имени
def db_read_name(exercname = None):
    if exercname is None:
        return None
    # end

    if Exercise.objects.filter(Name = exercname).exists():
        exerc = Exercise.objects.filter(Name = exercname)
        return exerc
    else:
        return None
    # end
# end

# Обновляем упражнение
def db_update(exercid = None, new_name = None, new_task = None, new_content = None, new_answer = None, new_catg = None):
    if exercid is None:
        return None
    # end

    if db_exists(exercid):
        exerc = Exercise.objects.get(exercid=exercid)
        if new_name is not None:
            exerc.Name = new_name
        # end

        if new_task is not None:
            exerc.Task = new_task
        # end

        if new_content is not None:
            exerc.Content = new_content
        # end

        if new_answer is not None:
            exerc.Answer = new_answer
        # end

        if new_catg is not None:
            exerc.Catg = new_catg
        # end

        exerc.save()
        return exerc
    else:
        return None
    # end
# end

# Удаляем упражнение
def db_delete(exercid = None):
    if exercid is None:
        return None
    # end

    if db_exists(exercid):
        exerc = Exercise.objects.get(exercid=exercid)
        exerc.delete()
        return exercid
    else:
        return None
    # end
# end

# Очищаем таблицу
def db_delete_all():
    Exercise.objects.all().delete()
# end

# Инициализируем таблицу правил, считывая файл заданного формата
def db_initialize(file_name):
    DBinidata = iniDB_routine.iniDB(file_name, 5)
    ctgs = RECr.db_initialize(DBinidata[:, 0])
    for k in range(DBinidata.shape[0]):
        db_create(name = DBinidata[k, 1].replace('\n', ''),
                  task = DBinidata[k, 2],
                  content = DBinidata[k, 3],
                  answer = DBinidata[k, 4].replace('\n', ''),
                  catg = ctgs[k])
    # end
#end


