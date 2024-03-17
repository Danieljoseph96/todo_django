from django.db import models

# Create your models here.
class Todo(models.Model):
    crital=1
    normal=0
    type_level=[
        (crital, 'crital'),
        (normal, 'normal'),
    ]
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    type=models.IntegerField(choices=type_level, default=normal)  
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title