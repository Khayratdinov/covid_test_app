from django.contrib import admin
from client.models import Client





class ClientAdmin(admin.ModelAdmin):
    list_display = ( "name","surname", 'time_deadline', 'created_at',)
    list_display_links = ("name",)
    exclude = ('qr_code', 'qr_url', 'time_deadline')
    list_filter = ("gender", "time_deadline")
    search_fields = ("name", "surname",)
    list_per_page = 20
    list_max_show_all = 100

 
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'url', None) is None:
            obj.qr_url = request.get_host()
        obj.save()


        
# Register your models here.
admin.site.register(Client, ClientAdmin)


