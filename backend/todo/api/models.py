from django.db import models


class Tasks(models.Model):
    title = models.CharField('title', max_length=150)
    description = models.TextField('decription', max_length=500)
    deadline = models.DateField('dead line')
    completed_at = models.DateField('completed at', null=True, blank=True)

    class Meta:
        verbose_name = 'todo'
        verbose_name_plural = 'todos'
        ordering = ('completed_at', 'deadline')
