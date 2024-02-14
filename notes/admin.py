from django.contrib import admin
from .models import CustomUser, Note

admin.site.register(CustomUser)
admin.site.register(Note)
