from django.db import models

# Create your models here.


class PersonInfo(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    hireDate = models.DateField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '人员信息'


class Vocation(models.Model):
    id = models.AutoField(primary_key=True)
    job = models.CharField(max_length=20)
    title = models.CharField(max_length=20)
    payment = models.IntegerField(null=True, blank=True)
    name = models.ForeignKey(PersonInfo, on_delete=models.CASCADE, related_name='ps')

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '职业信息'


#省份
class Province(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return str(self.name)


# 城市
class City(models.Model):
    name = models.CharField(max_length=20)
    province = models.ForeignKey(Province, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.name)


# 人物
class Person(models.Model):
    name = models.CharField(max_length=20)
    living = models.ForeignKey(City, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.name)


# 员
class Performer(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    nationality = models.CharField(max_length=20)

    def __str__(self):
        return str(self.name)


# 节目
class Program(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    performer = models.ManyToManyField(Performer)
    
    def __str__(self):
        return str(self.name)


