from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from coupons.models import Coupon
from coupons.forms import CouponApplyForm
from django.utils import timezone


@require_POST
def coupon_apply(request):
    time_now = timezone.now()
    form = CouponApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        coupon = Coupon.objects.get(code__iexact=code,
                                    valid_from__lte=time_now,
                                    valid_to__gte=time_now,
                                    active=True)
        if coupon:
            request.session['coupon_id'] = coupon.id
        else:
            request.session['coupon_id'] = None
    return redirect('cart:cart_detail')




