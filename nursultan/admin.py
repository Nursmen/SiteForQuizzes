from django.contrib import admin
from . import models

# Register your models here.
admin.site.register(models.Test)
admin.site.register(models.Queston)
admin.site.register(models.Scores)