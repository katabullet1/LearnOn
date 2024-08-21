from django.contrib import admin

# Register your models here.
from .models import Messages, Room, Notes

admin.site.register(Messages)
admin.site.register(Room)

admin.site.register(Notes)
# admin.site.register(SampleImage)