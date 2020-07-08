from django.contrib import admin
from .models import Options
from .models import Pushes

class OptionsAdmin(admin.ModelAdmin):
    list_display = ("name", "value")

class PushesAdmin(admin.ModelAdmin):
    change_form_template = "notification/change_form_preview.html"
    def eu_date(self, obj):
        return obj.date_pushed.strftime("%d/%m/%y")
    eu_date.admin_order_field = 'date_pushed'
    eu_date.short_description = 'Дата отправки' 

    fields = ("title", "text", "date_pushed", "picture", "name", "count")
    list_display = ("title", "text", 'date_created', "eu_date", "name", "count")

admin.site.register(Options, OptionsAdmin)
admin.site.register(Pushes, PushesAdmin)