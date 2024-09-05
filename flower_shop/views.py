from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from flower_shop.forms import OrderForm
from flower_shop.models import *

from rest_framework import viewsets
from flower_shop.serializer import *


def home(request):
    return render(request, 'flower_shop/index.html')


class FlowerList(ListView):
    model = FlowerBouquet
    template_name = 'flower_shop/flower/list.html'
    allow_empty = True
    paginate_by = 6

    def get_queryset(self):
        return FlowerBouquet.objects.filter(is_exists=True)


class FlowerDetail(DetailView):
    model = FlowerBouquet
    template_name = 'flower_shop/flower/detail.html'


class GreenList(ListView):
    model = GreenType
    template_name = 'flower_shop/green/list.html'
    allow_empty = True
    paginate_by = 12


class GreenDetail(DetailView):
    model = GreenType
    template_name = 'flower_shop/green/detail.html'


class OrderList(ListView):
    model = Order
    template_name = 'flower_shop/order/list.html'
    allow_empty = True
    paginate_by = 6


class OrderCreate(CreateView):
    model = Order
    template_name = 'flower_shop/order/create.html'
    form_class = OrderForm


class OrderDetail(DetailView):
    model = Order
    template_name = 'flower_shop/order/detail.html'


class SupplierList(ListView):
    model = Supplier
    template_name = 'flower_shop/supplier/list.html'
    allow_empty = True
    paginate_by = 12


class SupplierDetail(DetailView):
    model = Supplier
    template_name = 'flower_shop/supplier/detail.html'


# _____________________________API_____________________________


class GreenTypeViewSet(viewsets.ModelViewSet):
    queryset = GreenType.objects.all()
    serializer_class = GreenTypeSerializer


class HolidayViewSet(viewsets.ModelViewSet):
    queryset = HolidayCollection.objects.all()
    serializer_class = HolidaySerializer


class FlowerBouquetViewSet(viewsets.ModelViewSet):
    queryset = FlowerBouquet.objects.all()
    serializer_class = FlowerSerializer


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class SupplyViewSet(viewsets.ModelViewSet):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer


class PosOrderViewSet(viewsets.ModelViewSet):
    queryset = PosOrder.objects.all()
    serializer_class = PosOrderSerializer


class PosSupplyViewSet(viewsets.ModelViewSet):
    queryset = PosSupply.objects.all()
    serializer_class = PosSupplySerializer
