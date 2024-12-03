from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product
from cart.forms import CartAddProductForm
from shop.filters import SearchFilter


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True).order_by('name')

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

        # фильтр
    product_filter = SearchFilter(request.GET, queryset=products)
    products = product_filter.qs

    return render(request,
                  'shop/product/list.html',
                  {'category': category,
                   'categories': categories,
                   'products': products,
                   'filter': product_filter})


def product_detail(request, id, slug):
    product = get_object_or_404(Product,
                                id=id,
                                slug=slug,
                                available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product, 'cart_product_form': cart_product_form})