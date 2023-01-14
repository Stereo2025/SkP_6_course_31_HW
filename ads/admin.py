from django.contrib import admin

# Register your models here.
from ads.models import Category, Ad, Selection

admin.site.register(Category)
admin.site.register(Ad)
admin.site.register(Selection)
