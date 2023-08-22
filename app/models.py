from django.db import models

# Create your models here.
    
class Group(models.Model):
    group_id = models.AutoField(primary_key=True)
    group_name = models.CharField(max_length=100)
    containt = models.TextField()
    created = models.DateField(auto_now=True)

    def __str__(self):
        return self.group_name

