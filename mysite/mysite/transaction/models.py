from django.db import models
from shop.models import Product
from django.urls import reverse

class Transaction(models.Model):
    id_sp = models.DecimalField(max_digits=1000, decimal_places=0)
    transaction_code = models.CharField(max_length=32)
    fullName = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=500)
    attachment = models.ImageField(upload_to='attachments/%Y/%m/%d', blank=True)
    customer_username = models.CharField(max_length=32)
    receiver_username = models.CharField(max_length=32)
    status = models.DecimalField(decimal_places=0, max_digits=1 ,default=2)


    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Order {}'.format(self.id)

    # def get_absolute_url(self):
    #     return reverse('transaction:transaction_create', args=[self.id_sp])
    # def get_total_cost(self):
    #     return sum(item.get_cost() for item in self.items.all())


# class OrderItem(models.Model):
#     order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
#     product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     quantity = models.PositiveIntegerField(default=1)

#     def __str__(self):
#         return '{}'.format(self.id)

#     def get_cost(self):
#         return self.price * self.quantity
