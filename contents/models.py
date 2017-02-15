from django.db import models


class University(models.Model):
    class Meta:
        verbose_name = "دانشگاه"

    name = models.CharField('نام', max_length=50)
    description = models.CharField('توضیح', max_length=5000)
    country = models.CharField('کشور', max_length=50)
    city = models.CharField('شهر', max_length=50)
    rank = models.IntegerField('رتبه')
    image = models.ImageField('عکس', upload_to='images/university/')

    def __str__(self):
        return self.name


class Field(models.Model):
    class Meta:
        verbose_name = "رشته"

    name = models.CharField('نام', max_length=50)
    description = models.CharField('توضیح', max_length=5000)
    image = models.ImageField('عکس', upload_to='images/field/')

    def __str__(self):
        return self.name


class Program(models.Model):
    class Meta:
        verbose_name = "برنامه"

    name = models.CharField('نام', max_length=50)
    university = models.ForeignKey(University,
                                   on_delete=models.CASCADE)
    field = models.ForeignKey(Field, on_delete=models.CASCADE)
    description = models.CharField('توضیح', max_length=5000)
    DEGREE = (('M', 'Master'),
              ('P', 'PHD'))
    degree = models.CharField('مقطع', max_length=1, choices=DEGREE)
    minimum_toefl = models.IntegerField('حداقل تافل')
    other_prerequisite = models.CharField('ساید پیشنیازها', max_length=5000)

    def __str__(self):
        return self.name
