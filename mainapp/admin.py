from django.contrib import admin
from mainapp.models import (
    Worker, TradePoint, Visit,
)

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )
    list_display = (
        "id", 
        'name',
        'phone_number',
    )
    
@admin.register(TradePoint)
class TradePointrAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )
    list_display = (
        "id", 
        'name',
    )
    
    
@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    search_fields = (
        'trade_point__name',
        'trade_point__worker__name'
    )
    list_display = (
        "id", 
        'visit_time',
        'latitude',
        'longitude',
    )