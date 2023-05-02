from django.db import models

class RECategory(models.Model):
    ctgid = models.IntegerField(primary_key=True)
    Name = models.TextField()

    def __str__(self):
        return self.Name
    # end
# end

class Rule(models.Model):
    ruleid = models.IntegerField(primary_key=True)
    Catg = models.ForeignKey('RECategory', on_delete=models.DO_NOTHING, null=True)
    Name = models.TextField()
    Description = models.TextField()
    Examples = models.TextField()
    Summary = models.TextField()

    def __str__(self):
        name = f'<b>{self.Name}</b>'
        descr = f'{self.Description}'
        exmpls_head = f'<b>Примеры</b>\n'
        exmpls = f'{self.Examples}'
        sum_head = f'<b>Кратко</b>\n'
        sum = f'{self.Summary}'

        ans = name + descr + exmpls_head + exmpls + sum_head + sum
        return ans
    # end
# end

class Exercise(models.Model):
    exid = models.IntegerField(primary_key=True)
    Name = models.TextField()
    Catg = models.ForeignKey('RECategory', on_delete=models.DO_NOTHING, null=True)
    Task = models.TextField()
    Content = models.TextField()
    Answer = models.TextField()

    def __str__(self):
        tsk = f'<b>{self.Name}.</b> {self.Task}\n'
        cntnt = f'{self.Content}'

        ans = tsk + cntnt
        return ans
    # end
# end

class User(models.Model):
    upk = models.IntegerField(primary_key=True)
    uid = models.IntegerField(default=0, unique=True)
# end

class WCategory(models.Model):
    ctgid = models.IntegerField(primary_key=True)
    ctg_uid = models.ForeignKey('User', on_delete=models.DO_NOTHING, null=True)
    Name = models.TextField()

    def __str__(self):
        return self.Name
    # end

# end


class Dictionary(models.Model):
    wid = models.IntegerField(primary_key=True)
    word_uid = models.ForeignKey('User', on_delete=models.DO_NOTHING)
    Catg = models.ForeignKey('WCategory', on_delete=models.CASCADE, null=True)
    WordForeign = models.TextField()
    WordRussian = models.TextField()

    def __str__(self):
        ansstr = '<b>'+self.WordForeign+'</b>' + ' -- ' + self.WordRussian
        return ansstr
    # end

    def save(self, *args, **kwargs):
        if self.Catg is None:
            if not(WCategory.objects.filter(Name = 'Пустая категория', ctg_uid = self.word_uid).exists()):
                tcatg = WCategory(Name = 'Пустая категория', ctg_uid = self.word_uid)
                tcatg.save()
            # end
            catg = WCategory.objects.filter(Name = 'Пустая категория', ctg_uid = self.word_uid)[0]

            self.Catg = catg
        super().save(*args, **kwargs)
    # end
# end

class Statistics(models.Model):
    pass

    def __str__(self):
        pass
    # end
# end
