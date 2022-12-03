from django.shortcuts import render
from .models import Transaction
from shop.models import Product
from .forms import TransactionForm
from django.contrib import messages
from django.shortcuts import render, redirect
from uuid import uuid4
# Create your views here.

def transaction_create(request, id_sp):
    if (request.session.get('user', None) == None):
        return redirect('account:login')

    transaction = Transaction(request)
    if request.method == 'POST':
        form = TransactionForm(request.POST ,request.FILES)
        if form.is_valid():
            transaction = form.save(commit=False)
            # order.total_cost = cart.get_total_price()
            transaction.transaction_code = uuid4().hex
            transaction.id_sp = id_sp
            transaction.status = 2
            transaction.customer_username = request.session.get('user')
            transaction.save()

            return render(request, 'transaction/created.html', {'transaction': transaction})
        else:
            messages.error(request, 'Invalid input')
    else:
        form = TransactionForm()
        product = Product.objects.filter(id=id_sp)[0]
    return render(request, 'transaction/create.html', {'form': form, 'product': product})


def transaction_list(request):
    sort = ['-created']
    limit = 10
    offset = 0
    if 'sort' in request.GET:
        sort = request.GET.getlist('sort')
    if 'limit' in request.GET:
        limit = int(request.GET.get('limit'))
    if 'offset' in request.GET:
        offset = int(request.GET.get('offset'))

    orders = Order.objects.all().order_by(*sort)[offset:limit+offset]
    context = {'orders': orders, 'sort': sort, 'limit': limit}
    return render(request, 'transaction/updates.html', context)


def transaction_detail(request):
    order_code = request.GET.get('order_code')
    order = Order.objects.filter(order_code=order_code).first()
    items = order.items.all() if order else None
    context = {'order_code': order_code, 'order': order, 'items': items}
    return render(request, 'order/details.html', context)