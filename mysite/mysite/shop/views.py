from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product
from django.contrib import messages


def product_list(request, category_slug=None):
    sort = ['-created']
    limit = 10
    category = None 
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    if 'sort' in request.GET:
        sort = request.GET.getlist('sort')
    if 'limit' in request.GET:
        limit = int(request.GET.get('limit'))

    products = products.order_by(*sort)[:limit]
    context = {'category': category, 'categories': categories, 'products': products, 'sort': sort, 'limit': limit}
    return render(request, 'shop/product/list.html', context)


def product_detail(request, id, slug):
    if request.method == 'POST':
        product = Product.objects.filter(id=id).first()
        if product.owner == request.session['user']:
            messages.error(request, 'You cannot order your own product')
            return render(request, 'shop/product/detail.html', {'product': product})
        else:
            return redirect('transaction:transaction_create', id_sp=id)
    else:
        product = get_object_or_404(Product, id=id, slug=slug, available=True)
        context = {'product': product}
        return render(request, 'shop/product/detail.html', context)

def about(request):
    return render(request,'shop/base/about.html')