from django.urls import path
from .views import *

from django.urls import include
from rest_framework import routers

urlpatterns = [
    path('catalog/', FlowerList.as_view(), name='flower_list'),
    path('catalog/<int:pk>/', FlowerDetail.as_view(), name='flower_detail'),
    path('green/', GreenList.as_view(), name='green_list'),
    path('green/<int:pk>/', GreenDetail.as_view(), name='green_detail'),
    path('supplier/', SupplierList.as_view(), name='supplier_list'),
    path('supplier/<int:pk>/', SupplierDetail.as_view(), name='supplier_detail'),
]

router = routers.SimpleRouter()
router.register('api/green_type', GreenTypeViewSet, basename='green_type')
router.register('api/holiday_collection', HolidayViewSet, basename='holiday_collection')
router.register('api/flower_bouquet', FlowerBouquetViewSet, basename='flower_bouquet')
router.register('api/supplier', SupplierViewSet, basename='supplier')
router.register('api/order', OrderViewSet, basename='order')
router.register('api/supply', SupplyViewSet, basename='supply')
router.register('api/pos_order', PosOrderViewSet, basename='pos_order')
router.register('api/pos_supply', PosSupplyViewSet, basename='pos_supply')
urlpatterns += router.urls
