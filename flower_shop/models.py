from django.db import models

MAX_LENGTH = 255


class GreenType(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название типа')
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    poison = models.BooleanField(default=False, verbose_name='Ядовитость')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип растения'
        verbose_name_plural = 'Типы растений'


class HolidayCollection(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название коллекции')
    description = models.TextField(verbose_name='Описание')
    date_start = models.DateField(auto_now_add=True, verbose_name='Дата начала')
    date_end = models.DateField(auto_now_add=True, verbose_name='Дата окончания')

    def __str__(self):
        return f"{self.name} - ({self.date_start} - {self.date_end})"

    class Meta:
        verbose_name = 'Коллекция к празднику'
        verbose_name_plural = 'Коллекции к праздникам'


class FlowerBouquet(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название букета')
    description = models.TextField(verbose_name='Описание')
    price = models.FloatField(verbose_name='Цена')
    flower_count = models.PositiveIntegerField(default=1, verbose_name='Количество цветков')
    color = models.CharField(max_length=MAX_LENGTH, verbose_name='Основной цвет')
    photo = models.ImageField(upload_to='image/%Y/%m/%d', null=True, blank=True, verbose_name='Изображение')
    is_exists = models.BooleanField(default=True, verbose_name='Доступность для заказа')

    def __str__(self):
        return f"{self.name} - {self.price} руб. - {self.flower_count} шт."

    class Meta:
        verbose_name = 'Букет'
        verbose_name_plural = 'Букеты'


class Supplier(models.Model):
    name = models.CharField(max_length=MAX_LENGTH, verbose_name='Название')
    agent_firstname = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия представителя')
    agent_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя представителя')
    phone = models.CharField(max_length=16, verbose_name='Телефон')
    address = models.CharField(max_length=MAX_LENGTH, verbose_name='Адрес')
    is_exists = models.BooleanField(default=True, verbose_name='Доступность')
    country = models.CharField(max_length=MAX_LENGTH, verbose_name='Страна отгрузки')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'


class Order(models.Model):
    SHOP = "SH"
    COURIER = "CR"
    TYPE_DELIVERY = [
        (SHOP, 'Магазин'),
        (COURIER, 'Курьер'),
    ]
    buyer_firstname = models.CharField(max_length=MAX_LENGTH, verbose_name='Фамилия заказчика')
    buyer_name = models.CharField(max_length=MAX_LENGTH, verbose_name='Имя заказчика')
    comment = models.CharField(null=True, blank=True, max_length=MAX_LENGTH, verbose_name='Комментарий')
    delivery_address = models.CharField(max_length=MAX_LENGTH, verbose_name='Адрес доставки')
    delivery_type = models.CharField(max_length=2, choices=TYPE_DELIVERY, default=SHOP, verbose_name='Способ доставки')
    date_start = models.DateField(auto_now_add=True, verbose_name='Дата начала')
    finish = models.BooleanField(default=False, verbose_name='Выполнен')

    bouquet = models.ManyToManyField('FlowerBouquet', through='PosOrder', verbose_name='Букет')

    def __str__(self):
        return f'№{self.pk} ({self.buyer_firstname} {self.buyer_name} ({self.date_start}))'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Supply(models.Model):
    date_supply = models.DateTimeField(verbose_name='Дата поставки')
    supplier = models.ForeignKey(Supplier, on_delete=models.PROTECT, verbose_name='Поставщик')
    green = models.ManyToManyField(GreenType, through='PosSupply', verbose_name='Цветы')

    def __str__(self):
        return f'№{self.pk} ({self.date_supply} {self.green.name})'

    class Meta:
        verbose_name = 'Поставка'
        verbose_name_plural = 'Поставки'


class PosOrder(models.Model):
    bouquet = models.ForeignKey(FlowerBouquet, on_delete=models.PROTECT, verbose_name='Букет')
    order = models.ForeignKey(Order, on_delete=models.PROTECT, verbose_name='Заказ')

    count = models.PositiveIntegerField(default=1, verbose_name='Количество')
    discount = models.PositiveIntegerField(default=0, verbose_name='Скидка на товар')

    def __str__(self):
        return f'№{self.order.pk} ({self.bouquet.name} -{self.order.buyer_name} {self.order.buyer_firstname})'

    class Meta:
        verbose_name = 'Позиция заказа'
        verbose_name_plural = 'Позиции заказа'


class PosSupply(models.Model):
    green = models.ForeignKey(GreenType, on_delete=models.PROTECT, verbose_name='Растение')
    supply = models.ForeignKey(Supply, on_delete=models.PROTECT, verbose_name='Поставка')

    count = models.PositiveIntegerField(default=1, verbose_name='Количество')

    def __str__(self):
        return f'{self.green.name} - #{self.supply.pk} ({self.supply.date_supply})'

    class Meta:
        verbose_name = 'Позиция поставки'
        verbose_name_plural = 'Позиции поставки'
