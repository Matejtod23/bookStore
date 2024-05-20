from django.contrib import admin
from .models import PublicationHouse, Book


# Register your models here.
class PublicationHouseAdmin(admin.ModelAdmin):
    pass


class BookAdmin(admin.ModelAdmin):
    pass


admin.site.register(PublicationHouse, PublicationHouseAdmin)
admin.site.register(Book, BookAdmin)
