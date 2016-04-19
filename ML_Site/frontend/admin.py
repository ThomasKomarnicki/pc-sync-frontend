from django.contrib import admin
from .models import Faq


class FaqAdmin(admin.ModelAdmin):
    pass
admin.site.register(Faq, FaqAdmin)
