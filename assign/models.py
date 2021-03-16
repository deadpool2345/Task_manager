from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


STATUS=(
    ('A','assigned'),
    ('O','ongoing'),
    ('C','completed')

)
class Task(models.Model):
    assigner=models.ForeignKey(User,on_delete=models.CASCADE)
    users=models.ManyToManyField(User,related_name='users')
    name=models.CharField(max_length=255)
    description=models.TextField()
    status=models.CharField(max_length=1,choices=STATUS)

    def __str__(self):
        return f'{self.name}'