from django.contrib import admin
from .models import *


@admin.register(GreenType)
class GreenTypeAdmin(admin.ModelAdmin):
    pass


@admin.register(HolidayCollection)
class HolidayCollectionAdmin(admin.ModelAdmin):
    pass


@admin.register(FlowerBouquet)
class FlowerBouquetAdmin(admin.ModelAdmin):
    pass


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass


@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    pass


@admin.register(PosOrder)
class PosOrderAdmin(admin.ModelAdmin):
    pass


@admin.register(PosSupply)
class PosSupplyAdmin(admin.ModelAdmin):
    pass
