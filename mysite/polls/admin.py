from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Question, Choice, User, QiangDaItem

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(User)
admin.site.register(QiangDaItem)