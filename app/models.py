from django.db import models

# Create your models here.
    
class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=100)
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.group_name

class Chat(models.Model):
    chat_id = models.AutoField(primary_key=True)
    containt = models.CharField(max_length=500)
    timestamp = models.DateTimeField(auto_now=True)
    group = models.ForeignKey(Group,on_delete=models.CASCADE)

    def  __str__(self):
        return self.containt

