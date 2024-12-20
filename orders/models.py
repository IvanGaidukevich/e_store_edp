from django.db import models
from django.contrib.auth.models import User # new
from shop.models import Product
from accounts.models import Address
from coupons.models import Coupon


ORDER_STATUS_CHOICES = (
    ('active', 'Активный'),      # Заказ создан
    ('completed', 'Выполненный'),  # Заказ успешно завершён
    ('canceled', 'Отменённый'),   # Заказ отменён пользователем
)


class Order(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=40, verbose_name='Фамилия')
    phone = models.CharField(max_length=11, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Email')
    shipping_address = models.ForeignKey(Address, related_name='shipping_address',
                                         on_delete=models.CASCADE,
                                         verbose_name="Адрес доставки")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создан')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлен')
    paid = models.BooleanField(default=False, verbose_name='Статус оплаты')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=20,
                              choices=ORDER_STATUS_CHOICES,
                              default='active',
                              verbose_name='Cтатус заказа')

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'Order №: {self.id}'

    def get_total_cost(self):
        return sum(item.total_price() for item in self.orderitem_set.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.id}'

    def total_price(self):
        return self.price * self.quantity


