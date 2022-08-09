from django.contrib import admin

from AnimalShop.models import AnimalDetail, Animal


class AnimalDetailAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'weight', 'height', 'color', 'behaviour', 'nutrition')


class AnimalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'race', 'detailsID')


admin.site.register(AnimalDetail, AnimalDetailAdmin)
admin.site.register(Animal, AnimalAdmin)
