from django.contrib import admin
from .models import Pet


class PetAdmin(admin.ModelAdmin):
    list_display = ['name', 'get_donor', 'get_adopter']

    def get_donor(self, obj):
        return obj.donor.name
    get_donor.short_description = 'Dono'

    def get_adopter(self, obj):
        if obj.adopter:
            return obj.adopter.name
    get_adopter.short_description = 'Adotante'
    

    search_fields = ['name', 'donor__name', 'adopter__name', 'chip', 'sex', 'age', 'species', 'breed']
    list_filter = ['adopted']

admin.site.register(Pet, PetAdmin)