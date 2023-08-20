from django.contrib import admin
from .models import Advertisement
from django.utils.html import format_html
class AdvertisementAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price', 'created_date','updated_date', 'auction','img']
    list_filter = ['auction', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true']

    @admin.action(description='Убрать возможность торга ')
    def make_auction_as_false(self, request, queryset):
        queryset.update (auction = False)


    @admin.action(description='Добавить возможность торга ')
    def make_auction_as_true(self, request, queryset):
        queryset.update(auction=True)

    @admin.display()
    def img(self,obj):
        if obj.image:
            return format_html('<img src="{}" width="80">'.format(obj.image.url))
        else:
            return format_html('<img src="{}" width="80">'.format("/static/img/pict.png"))

    fieldsets = (
        ('Общее',{'fields': ('title', 'description','image'), 'classes': ['collapse']}),
        ('Финансы', {'fields': ('price','auction'), 'classes': ['collapse']})
    )

admin.site.register(Advertisement,AdvertisementAdmin)

