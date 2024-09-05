from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

from flower_shop.forms import OrderForm
from flower_shop.models import *

from rest_framework import viewsets
from flower_shop.serializer import *

from django.contrib.auth.decorators import login_required, permission_required
from django.utils.decorators import method_decorator


def home(request):
    return render(request, 'flower_shop/index.html')


class FlowerList(ListView):
    model = FlowerBouquet
    template_name = 'flower_shop/flower/list.html'
    allow_empty = True
    paginate_by = 6

    def get_queryset(self):
        return FlowerBouquet.objects.filter(is_exists=True)


@method_decorator(login_required(), name='dispatch')
@method_decorator(permission_required('flower_shop.view_flowerbouquet'), name='dispatch')
class FlowerDetail(DetailView):
    model = FlowerBouquet
    template_name = 'flower_shop/flower/detail.html'


@method_decorator(login_required(), name='dispatch')
@method_decorator(permission_required('flower_shop.view_greentype'), name='dispatch')
class GreenList(ListView):
    model = GreenType
    template_name = 'flower_shop/green/list.html'
    allow_empty = True
    paginate_by = 12


@method_decorator(login_required(), name='dispatch')
@method_decorator(permission_required('flower_shop.view_greentype'), name='dispatch')
class GreenDetail(DetailView):
    model = GreenType
    template_name = 'flower_shop/green/detail.html'


@method_decorator(login_required(), name='dispatch')
class OrderList(ListView):
    model = Order
    template_name = 'flower_shop/order/list.html'
    allow_empty = True
    paginate_by = 6


@method_decorator(login_required(), name='dispatch')
class OrderCreate(CreateView):
    model = Order
    template_name = 'flower_shop/order/create.html'
    form_class = OrderForm


@method_decorator(login_required(), name='dispatch')
class OrderDetail(DetailView):
    model = Order
    template_name = 'flower_shop/order/detail.html'


@method_decorator(login_required(), name='dispatch')
@method_decorator(permission_required('flower_shop.view_supplier'), name='dispatch')
class SupplierList(ListView):
    model = Supplier
    template_name = 'flower_shop/supplier/list.html'
    allow_empty = True
    paginate_by = 12


@method_decorator(login_required(), name='dispatch')
@method_decorator(permission_required('flower_shop.view_supplier'), name='dispatch')
class SupplierDetail(DetailView):
    model = Supplier
    template_name = 'flower_shop/supplier/detail.html'


# _____________________________API_____________________________
from rest_framework import permissions


class CustomPermissions(permissions.DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
        'HEAD': ['%(app_label)s.view_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }


class GreenTypeViewSet(viewsets.ModelViewSet):
    queryset = GreenType.objects.all()
    serializer_class = GreenTypeSerializer
    permission_classes = [CustomPermissions]


class HolidayViewSet(viewsets.ModelViewSet):
    queryset = HolidayCollection.objects.all()
    serializer_class = HolidaySerializer
    permission_classes = [CustomPermissions]


class FlowerBouquetViewSet(viewsets.ModelViewSet):
    queryset = FlowerBouquet.objects.all()
    serializer_class = FlowerSerializer
    permission_classes = [CustomPermissions]


class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [CustomPermissions]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [CustomPermissions]


class SupplyViewSet(viewsets.ModelViewSet):
    queryset = Supply.objects.all()
    serializer_class = SupplySerializer
    permission_classes = [CustomPermissions]


class PosOrderViewSet(viewsets.ModelViewSet):
    queryset = PosOrder.objects.all()
    serializer_class = PosOrderSerializer
    permission_classes = [CustomPermissions]


class PosSupplyViewSet(viewsets.ModelViewSet):
    queryset = PosSupply.objects.all()
    serializer_class = PosSupplySerializer
    permission_classes = [CustomPermissions]
