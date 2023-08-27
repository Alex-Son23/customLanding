from django.contrib import admin
from .models import DisplayModel, HeaderModel, TextModel, ImageModel, LinkModel, ButtonModel, CardModel, FormModel


# Register your models here.

class HeaderModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'display', 'text')  # Отображаемые поля в списке
    list_filter = ('display',)  # Поле для фильтрации


class TextModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'display', 'text')  # Отображаемые поля в списке
    list_filter = ('display',)  # Поле для фильтрации


class ImageModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'display', 'alt', 'title')  # Отображаемые поля в списке
    list_filter = ('display',)  # Поле для фильтрации


class LinkModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'text', 'href')  # Отображаемые поля в списке
    list_filter = ('display',)  # Поле для фильтрации


class ButtonModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'visible', 'text', 'href')  # Отображаемые поля в списке
    list_filter = ('display',)  # Поле для фильтрации
    

class FormModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'mail_to')  # Отображаемые поля в списке


# class CardModelAdmin(admin.ModelAdmin):
#     list_display = ('title', 'visible', 'text', 'href')  # Отображаемые поля в списке


admin.site.register(DisplayModel)
admin.site.register(HeaderModel, HeaderModelAdmin)
admin.site.register(TextModel, TextModelAdmin)
admin.site.register(ImageModel, ImageModelAdmin)
admin.site.register(LinkModel, LinkModelAdmin)
admin.site.register(ButtonModel, ButtonModelAdmin)
admin.site.register(CardModel)
admin.site.register(FormModel, FormModelAdmin)