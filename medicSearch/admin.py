from django.contrib import admin
from .models import *
# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'birthday')
    list_display_links = ('user','role')
    empty_value_display = 'vazio'
    list_filter = ('user__is_active',)
    readonly_field = ('user')
    search_fields = ('user__username',)

    fields = ('user', ('role', ), 'image', 'birthday', 'specialities', 'addresses', )
    #filtro de hierarquia com datas
    #date_hierarchy = 'created_at'
    

admin.site.register(Profile, ProfileAdmin)
admin.site.register(State)
admin.site.register(City)
admin.site.register(Neighborhood)
admin.site.register(Address)
admin.site.register(DayWeek)
admin.site.register(Rating)
admin.site.register(Speciality)