from accounts.models import Endereco, MyUser
from django.contrib import admin
from django.contrib.sessions.models import Session

admin.site.register(Session)

admin.site.register(MyUser)

admin.site.register(Endereco)