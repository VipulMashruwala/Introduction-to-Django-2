from django.db import models

# Create your models here.
class MyUser(models.Model):
    user_id = models.AutoField(primary_key= True)
    user_name = models.CharField(max_length = 20, null = False)
    user_address = models.CharField(max_length = 100, default= None)
    user_phone = models.CharField(max_length = 10, default= None)


class MyAdmin(models.Model):
    admin_id = models.AutoField(primary_key= True)
    admin_name = models.CharField(max_length= 20, null= False)
    admin_password = models.CharField(max_length= 20, null = False)

