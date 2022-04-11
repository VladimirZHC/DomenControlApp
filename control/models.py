from django.db import models


class ParamsSchema(models.Model):
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


class OrgUnit(models.Model):
    name = models.CharField('Подразделение', max_length=20)
    parent = models.ForeignKey(
        'self', 
        on_delete=models.CASCADE,
        related_name='children',
        verbose_name='Подразделение',
        blank=True,
        null=True,
        )
    group_policies = models.ManyToManyField(
        GroupPolicy,
        blank=True,
        related_name='orgunits',
        verbose_name='групповые политики',
    )

    def __str__(self):
        return f'Подразделение: {self.name}'
    
    def save(self, *args, **kwargs):
        if self.parent is None:
            self.parent = OrgUnit.objects.get(id=1)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Подразделение'
        verbose_name_plural = 'Подразделения'


class DomainUser(models.Model):
    name = models.CharField('Имя пользователя', max_length=20)
    login = models.CharField('Логин пользователя',max_length=20, unique=True, default='user1')
    orgunit = models.ForeignKey(
        OrgUnit,
        related_name='users', 
        on_delete=models.CASCADE,
        verbose_name='Подразделение',
        blank=True,
        null=True,
    )
    
    def __str__(self):
        return f'Пользователь {self.name}'
    
    def save(self, *args, **kwargs):
        if self.orgunit is None:
            self.orgunit = OrgUnit.objects.get(id=1)
        return super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = 'Пользователя'
        verbose_name_plural = 'Пользователи'


class Host(models.Model):
    name = models.CharField('Компьютеры', max_length=20)
    orgunit = models.ForeignKey(
        OrgUnit,
        related_name='hosts', 
        on_delete=models.CASCADE,
        verbose_name='Подразделение',
        blank=True,
        null=True,
    )

    def __str__(self):
        return f'Компьютер {self.name}'
    
    def save(self, *args, **kwargs):
        if self.orgunit is None:
            self.orgunit = OrgUnit.objects.get(id=1)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Компьютер'
        verbose_name_plural = 'Компьютеры'


ParamsSchema.objects.get_or_create(type="USER")
ParamsSchema.objects.get_or_create(type="HOST")
# OrgUnit.objects.get_or_create(name="root")