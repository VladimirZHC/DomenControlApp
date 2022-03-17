from __future__ import division
from django.db import models


class GroupPolicy(models.Model):
    name = models.CharField('Групповая политика', max_length=30, unique=True)
    body = models.TextField('Основной контент')
    search_fields = ['name']
    
    
    def __str__(self):
        return f'Групповая политика {self.name}'
    
    class Meta:
        ordering = ['name']
        verbose_name = 'Групповую политиику'
        verbose_name_plural = 'Групповые политики'
        
        
        
        
class Division(models.Model):
    name = models.CharField('Подразделение', max_length=20)
    divisions = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE,
        verbose_name='Подразделения',
        )
    group_policy = models.ManyToManyField(
        GroupPolicy,
        related_name='divisionof',
        blank=True,
        verbose_name='групповые политики',
    )
    
    
    def __str__(self):
        return f'Подразделение {self.name}'
    
    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'






class DomenUser(models.Model):
    name = models.CharField('Имя пользователя', max_length=20)
    division = models.ForeignKey(
        Division,
        related_name='domenuser', 
        on_delete=models.CASCADE,
        verbose_name='Подразделения',
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
        related_name='computers', 
        on_delete=models.CASCADE,
        verbose_name='Подразделения',
    )
    
    def __str__(self):
        return f'Компьютер {self.name}'
    
    class Meta:
        verbose_name = 'Компьютер'
        verbose_name_plural = 'Компьютеры'
        
        

