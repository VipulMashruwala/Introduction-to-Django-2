from django.contrib import admin
from .models import MyAdmin, MyUser

# Register your models here.
admin.site.register(MyUser)
admin.site.register(MyAdmin)