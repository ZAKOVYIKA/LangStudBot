from webhook.models import Rule
from webhook.models import RECategory
import numpy as np
from webhook.DB_Routines import iniDB_routine
import webhook.DB_Routines.RECtg_routines as RECr

# Проверяем, что запись существует в БД
def db_exists(value = None):
    if isinstance(value, float) | isinstance(value, int):
        return Rule.objects.filter(ruleid = value).exists()
    elif isinstance(value, str):
        return Rule.objects.filter(Name = value).exists()
    else:
        return False
    # end
# end

# Считываем внутренний номер правила
def db_id(name = None):
    if name is None:
        return None
    # end

    if Rule.objects.filter(Name = name).exists():
        rule = Rule.objects.filter(Name = name)
        return [rule[j].ruleid for j in range(len(rule))]
    else:
        return None
    # end
# end

# Создаём новое правило
def db_create(name = None, description = '', examples = '', summary = '', catg = None):
    if (name is None) | (catg is None):
        return None
    # end

    if db_exists(name):
        return None
    else:
        rule = Rule(Name = name, Description = description, Examples = examples, Summary = summary, Catg = catg)
        rule.save()
        return rule
    # end
# end

# Считываем правило по номеру
def db_read(ruleid = None):
    if ruleid is None:
        return None
    # end

    if db_exists(ruleid):
        rule = Rule.objects.get(ruleid=ruleid)
        return rule
    else:
        return None
    # end
# end

# Считываем правило по категории
def db_read_catg(rulecatg = None):
    if rulecatg is None:
        return None
    # end

    if Rule.objects.filter(Catg = rulecatg).exists():
        rule = Rule.objects.get(Catg = rulecatg)
        return rule
    else:
        return None
    # end
# end

# Обновляем правило
def db_update(ruleid = None, new_name = None, new_description = None, new_examples = None, new_summary = None, new_catg = None):
    if ruleid is None:
        return None
    # end

    if db_exists(ruleid):
        rule = Rule.objects.get(ruleid=ruleid)
        if new_name is not None:
            rule.Name = new_name
        # end

        if new_description is not None:
            rule.Description = new_description
        # end

        if new_examples is not None:
            rule.Examples = new_examples
        # end

        if new_summary is not None:
            rule.Summary = new_summary
        # end

        if new_catg is not None:
            rule.Catg = new_catg
        # end

        rule.save()
        return rule
    else:
        return None
    # end
# end

# Удаляем правило
def db_delete(ruleid = None):
    if ruleid is None:
        return None
    # end

    if db_exists(ruleid):
        rule = Rule.objects.get(ruleid=ruleid)
        rule.delete()
        return ruleid
    else:
        return None
    # end
# end

# Очищаем таблицу
def db_delete_all():
    Rule.objects.all().delete()
# end

# Инициализируем таблицу правил, считывая файл заданного формата
def db_initialize(file_name):
    DBinidata = iniDB_routine.iniDB(file_name, 5)
    ctgs = RECr.db_initialize(DBinidata[:, 0])
    for k in range(DBinidata.shape[0]):
        db_create(name = DBinidata[k, 1],
                  description = DBinidata[k, 2],
                  examples = DBinidata[k, 3],
                  summary = DBinidata[k, 4],
                  catg = ctgs[k])
    # end
#end


