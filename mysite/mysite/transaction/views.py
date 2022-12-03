from django.shortcuts import render
from .models import Transaction
from shop.models import Product
from .forms import TransactionForm
from django.contrib import messages
from django.shortcuts import render, redirect
from uuid import uuid4
# Create your views here.

def transaction_create(request, id_sp):
    product = Product.objects.filter(id=id_sp).first()
    if product.owner == request.session['user']:
        messages.error(request, 'You cannot order your own product')
        return render(request, 'shop/product/detail.html', {'product': product})

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
            transaction.customer_username = request.session['user']
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

class transaction_history:
    def __init__(self, image, productname, transactionID, description, status):
        self.image = image
        self.productname = productname
        self.transactionID = transactionID
        self.description = description
        self.status = status

def transaction_list(request):
    if (request.session.get('user', None) == None):
        return redirect('account:login')
    sort = ['-created']
    limit = 10
    offset = 0
    if 'sort' in request.GET:
        sort = request.GET.getlist('sort')
    if 'limit' in request.GET:
        limit = int(request.GET.get('limit'))
    if 'offset' in request.GET:
        offset = int(request.GET.get('offset'))

    customer_transactions = Transaction.objects.filter(customer_username = request.session['user']).all().order_by(*sort)[offset:limit+offset]
    transaction_history_arr = []
    for customer_transaction in customer_transactions:
        id_sp = customer_transaction.id_sp
        product = Product.objects.filter(id=id_sp).first()
        image = product.image
        productname = product.name
        transactionID = customer_transaction.transaction_code
        description = product.description
        status = customer_transaction.status
        transaction_history_arr.append(transaction_history(image, productname, transactionID, description, status))


    # owner_transactions = Transaction.objects.filter(customer_username = request.session['user']).all().order_by(*sort)[offset:limit+offset]
    results = Product.objects.filter(owner=request.session['user']).all().get("id")

    owner_transaction =  Transaction.objects.filter(id_sp__inrequest.session['user']).all().order_by(*sort)[offset:limit+offset]


    for owner_transaction in owner_transactions:
        id_sp = customer_transaction.id_sp
        product = Product.objects.filter(id=id_sp).first()
        image = product.image
        productname = product.name
        transactionID = customer_transaction.transaction_code
        description = product.description
        status = customer_transaction.status
        transaction_history_arr.append(transaction_history(image, productname, transactionID, description, status))

    context = {'transaction_history_arr': transaction_history_arr, 'sort': sort, 'limit': limit}
    return render(request, 'transaction/transactions.html', context)


def transaction_details(request, transaction_code):
    if (request.session.get('user', None) == None):
        return redirect('account:login')    
    transaction = Transaction.objects.filter(transaction_code=transaction_code).first()
    id_sp = transaction.id_sp

    product = Product.objects.filter(id=id_sp).first()


    context = {'transaction': transaction, 'product': product}
    return render(request, 'transaction/details.html', context)

def transaction_update(request):
    if (request.session.get('user', None) == None):
        return redirect('account:login')
    if request.method == 'POST':
        action = request.POST.get('action', None)
        transaction_code = request.POST.get('transaction_code', None)

        if (action is not None) and (transaction_code is not None):

            transaction = Transaction.objects.filter(transaction_code=transaction_code).first()

            if transaction is not None and transaction.status is 2:
                transaction.status = 1 if action=="Accept" else 0
                transaction.save()
        

        return redirect('transaction:transactions')