from django.contrib import admin
from .models import port

# Register your models here.
@admin.register(port)
class PortAdmin(admin.ModelAdmin):
    list_display=('name','email','subject','message','created_at')
