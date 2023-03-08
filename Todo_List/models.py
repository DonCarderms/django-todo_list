from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField('titulo', max_length=100)
    description = models.TextField('descricao', max_length=1000)
    completed = models.BooleanField('concluido', default=False)
    
    def update_status(self, value):
        self.completed = value

    def __str__(self):
        return self.title