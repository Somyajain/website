from django.contrib import admin

# Register your models here.

from .models import Recent_events,Teacher

admin.site.register(Recent_events)


admin.site.register(Teacher)
