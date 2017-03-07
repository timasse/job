from django.contrib import admin
from .models import Job, JobImage, JobPdf

class JobImageInline(admin.StackedInline):
    model = JobImage
    extra = 1

class JobPdfInline(admin.StackedInline):
    model = JobPdf
    extra = 1
	
class JobAdmin(admin.ModelAdmin):
    search_fields = ['client_phone']
    inlines = [JobImageInline, JobPdfInline, ]
	
admin.site.register(Job, JobAdmin)
