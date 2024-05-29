from django.contrib import admin
from .models import  Schedule, Hall, Client, Card, Service, Employee, WorkVakansiya, promocodes


class HallInline(admin.TabularInline):
    model = Hall
    extra = 0


class CardInline(admin.TabularInline):
    model = Card
    extra = 0




class ServiceInline(admin.TabularInline):
    model = Service
    extra = 0
    readonly_fields = ['service_name', 'service_start_date', 'service_end_date']




class HallAdmin(admin.ModelAdmin):
    list_display = ['name', 'price_per_night']


class ClientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'address', 'phone']
    inlines = [ServiceInline]

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name']

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ['start_work', 'end_work']

class WorkVakansiyaAdmin(admin.ModelAdmin):
    list_display = ['name', 'salary']

class CardAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_by', 'price', 'start_work', 'end_work']

    def get_halls(self, obj):
        return ', '.join(hall.name for hall in obj.halls.all())

    get_halls.short_description = 'Halls'


class ServiceAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'client', 'service_start_date', 'service_end_date']

class PromocodeAdmin(admin.ModelAdmin):
    list_display = ['skidka', 'price']

admin.site.register(promocodes, PromocodeAdmin)
admin.site.register(WorkVakansiya, WorkVakansiyaAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Hall, HallAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Card, CardAdmin)
admin.site.register(Service, ServiceAdmin)