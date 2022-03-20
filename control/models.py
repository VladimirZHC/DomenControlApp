from django.db import models



class SchemaParams(models.Model):
    TYPE_CHOICES = (
        ("HOST", "host"),
        ("USER", "user"),
    )
    type = models.SlugField('Типы', primary_key=True, allow_unicode=True, choices=TYPE_CHOICES, max_length=10, default='HOST')
    body = models.TextField('Содержимое схемы', null=True, blank=True, default="{}")
    
    def __str__(self):
        return f'Тип: {self.type}'
    
    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class GroupPolicy(models.Model):
    name = models.CharField('Групповая политика', max_length=30, unique=True)
    body = models.TextField('Содержимое политики', null=True, blank=True)
    search_fields = ['name']
    
    
    def __str__(self):
        return f'Групповая политика: {self.name}'
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Групповую политиику'
        verbose_name_plural = 'Групповые политики'
        
        
        
        
class Division(models.Model):
    name = models.CharField('Подразделение', max_length=20)
    divisions = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE,
        related_name='departament',
        verbose_name='Подразделения',
        blank=True,
        null=True,
        )
    group_policy = models.ManyToManyField(
        GroupPolicy,
        related_name='policy',
        blank=True,
        verbose_name='групповые политики',
    )
    types = models.ManyToManyField(
        SchemaParams,
        related_name='types',
        blank=True,
        verbose_name='Тип',
    )
    
    
    def __str__(self):
        return f'Подразделение: {self.name}'
    
    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'






class DomenUser(models.Model):
    name = models.CharField('Имя пользователя', max_length=20)
    division = models.ForeignKey(
        Division,
        related_name='userdevision', 
        on_delete=models.CASCADE,
        verbose_name='Подразделения',
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return f'Пользователь {self.name}'
    
    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'
        
        
        
        
class Computers(models.Model):
    name = models.CharField('Компьютеры', max_length=20)
    division = models.ForeignKey(
        Division,
        related_name='computerdivision', 
        on_delete=models.CASCADE,
        verbose_name='Подразделения',
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return f'Компьютер {self.name}'
    
    class Meta:
        verbose_name = 'Компьютер'
        verbose_name_plural = 'Компьютеры'
        
        

