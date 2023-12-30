from django.contrib import admin
from .models import Meseros

# Register your models here.
#admin.site.register(Meseros)

@admin.register(Meseros)
class MeserosAdmin(admin.ModelAdmin):
    pass

