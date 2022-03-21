from django.db import models

class Todos(models.Model):
    title = models.CharField(max_length=100)
    details = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Todos'


