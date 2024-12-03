from django.shortcuts import render, redirect
from cart.cart import Cart
from orders.forms import OrderCreateForm
from orders.models import OrderItem, Order
from django.contrib.auth.decorators import login_required  # new


@login_required
def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity']
                )
            cart.clear()
            return render(request, 'orders/order/success.html', {'order': order})
    else:
        user = request.user
        initial = {
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email,
            'phone': user.profile.tel
        }
        form = OrderCreateForm(initial=initial)
    return render(request, 'orders/order/creates.html', {'cart': cart, 'form': form})


@login_required
def cancel_order(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == 'POST':
        order.status = 'canceled'
        order.save()
        return redirect('accounts:profile_view')
    return render(request, 'orders/order/cancel_confirm.html', {'order': order})
