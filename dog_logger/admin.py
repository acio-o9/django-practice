from django.contrib import admin

from .models import Dog, Owner, ActionType, ActionHistory

# Register your models here.
admin.site.register(Dog)
admin.site.register(Owner)
admin.site.register(ActionType)
admin.site.register(ActionHistory)
