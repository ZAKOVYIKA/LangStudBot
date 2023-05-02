from webhook.models import Dictionary
import webhook.DB_Routines.WCtg_routines as WCr

# Проверяем, что запись существует в БД
def db_exists(value = None, uid = None):
    if isinstance(value, float) | isinstance(value, int):
        return Dictionary.objects.filter(wid = value, word_uid = uid).exists()
    elif isinstance(value, str):
        return (Dictionary.objects.filter(WordRussian = value, word_uid = uid).exists()) | (Dictionary.objects.filter(WordForeign = value, word_uid = uid).exists())
    else:
        return False
    # end
# end

# Считываем внутренний номер слова
def db_id(word = None, uid = None):
    if (word is None) | (uid is None):
        return None
    # end

    if Dictionary.objects.filter(WordRussian = word, word_uid = uid).exists():
        dicti = Dictionary.objects.filter(WordRussian = word, word_uid = uid)
        return [dicti[j].wid for j in range(len(dicti))]
    elif Dictionary.objects.filter(WordForeign = word, word_uid = uid).exists():
        dicti = Dictionary.objects.filter(WordForeign = word, word_uid = uid)
        return [dicti[j].wid for j in range(len(dicti))]
    else:
        return None
    # end
# end

# Считываем слова по категории
def db_read_catg(wordcatg = None, uid = None):
    if (wordcatg is None) | (uid is None):
        return None
    # end

    if Dictionary.objects.filter(Catg = wordcatg, word_uid = uid).exists():
        dicti = Dictionary.objects.filter(Catg = wordcatg, word_uid = uid)
        return dicti
    else:
        return None
    # end
# end

# Создаём новое слово
def db_create(uid = None, WordRussian = '', WordForeign = '', catg = None):
    if (uid is None):
        return None
    # end

    if db_exists(WordRussian, uid) | db_exists(WordForeign, uid):
        return None
    else:
        dicti = Dictionary(word_uid = uid, WordRussian = WordRussian, WordForeign = WordForeign, Catg = catg)
        dicti.save()
        return dicti
    # end
# end

# Считываем слово по номеру
def db_read(wid = None, uid = None):
    if (wid is None) | (uid is None):
        return None
    # end

    if db_exists(wid, uid):
        dicti = Dictionary.objects.get(wid=wid, word_uid = uid)
        return dicti
    else:
        return None
    # end
# end

# Считываем слово по слову
def db_read_word(word = None, uid = None):
    if (word is None) | (uid is None):
        return None
    # end

    if Dictionary.objects.filter(WordRussian = word, word_uid = uid).exists():
        dicti = Dictionary.objects.filter(WordRussian = word, word_uid = uid)
        return dicti
    elif Dictionary.objects.filter(WordForeign = word, word_uid = uid).exists():
        dicti = Dictionary.objects.filter(WordForeign=word, word_uid=uid)
        return dicti
    else:
        return None
    # end
# end

# Ищем слово по похожести к слову
def db_search_word(word = None, uid = None):
    if (word is None) | (uid is None):
        return None
    # end

    if Dictionary.objects.filter(WordRussian__contains = word, word_uid = uid).exists():
        dicti = Dictionary.objects.filter(WordRussian__contains = word, word_uid = uid)
        return dicti
    elif Dictionary.objects.filter(WordForeign__contains = word, word_uid = uid).exists():
        dicti = Dictionary.objects.filter(WordForeign__contains = word, word_uid=uid)
        return dicti
    else:
        return None
    # end
# end

# Обновляем слово
def db_update(wid = None, new_wr = None, new_wf = None, uid = None, new_catg = None):
    if (wid is None) | (uid is None):
        return None
    # end

    if db_exists(wid, uid):
        dicti = Dictionary.objects.get(wid=wid, word_uid = uid)
        print(dicti)
        if new_wr is not None:
            dicti.WordRussian = new_wr
        # end

        if new_wf is not None:
            dicti.WordForeign = new_wf
        # end

        if new_catg is not None:
            dicti.Catg = new_catg
        # end

        dicti.save()
        return dicti
    else:
        return None
    # end
# end

# Удаляем слово
def db_delete(wid = None, uid = None):
    if (wid is None) | (uid is None):
        return None
    # end

    if db_exists(wid, uid):
        dicti = Dictionary.objects.get(wid=wid, word_uid = uid)
        dicti.delete()
        return wid
    else:
        return None
    # end
# end

# Очищаем таблицу
def db_delete_all(uid = None):
    if uid is None:
        return None
    # end

    Dictionary.objects.filter(word_uid = uid).delete()
# end


