from django.contrib import admin

from orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
    fields = ['product', 'price', 'quantity']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'paid', 'created_at']
    list_filter = ['paid', 'created_at']
    inlines = [OrderItemInline]
