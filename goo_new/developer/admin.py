from django.contrib import admin
from .models import Developer, Application

# Register your models here.

class ApplicationInline(admin.TabularInline):
	model = Application

class DeveloperAdmin(admin.ModelAdmin):
	inlines = [
		ApplicationInline,
	]

admin.site.register(Developer, DeveloperAdmin)
admin.site.register(Application)