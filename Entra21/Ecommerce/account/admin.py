from account.forms import MyUserForm
from account.models import Endereco, MyUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

class MyUserAdmin(UserAdmin):
    form = MyUserForm
    

admin.site.register(MyUser, MyUserAdmin)
admin.site.register(Endereco)