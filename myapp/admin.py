from django.contrib import admin
from .models import Emp, Login, Register

# Register your models here.
admin.site.register(Emp)
admin.site.register(Register)
admin.site.register(Login)