from django.db import models
from django.contrib.auth import get_user_model
from base.models import Product
from cart.models import Cart, CartProduct


User = get_user_model()

ORDER_STATUS_CHOICES = (
    ('created', 'Створений'),
    ('paid', 'Оплачений'),
    ('shipped', 'Відправлений'),
    ('canceled', 'Відмінений'),
)

COUNTRIES = (
    ('Ukraine', 'Україна'),
    ('Poland', 'Польша'),
    ('Moldova', 'Молдова'),
)


class Order(models.Model):
    cart = models.OneToOneField(Cart, on_delete=models.CASCADE, null=True)
    subtotal = models.PositiveIntegerField()
    total = models.PositiveIntegerField()
    status = models.CharField(max_length=20, choices=ORDER_STATUS_CHOICES, default='created', null=False)
    timestamp = models.DateTimeField(auto_now_add=True, null=False)
    email = models.CharField(max_length=50, null=False, blank=True)
    first_name = models.CharField(max_length=50, null=False, blank=True)
    last_name = models.CharField(max_length=50, null=False, blank=True)
    phone = models.CharField(max_length=15, null=False, blank=True)
    address = models.CharField(max_length=200, null=False, blank=True)
    country = models.CharField(max_length=30, choices=COUNTRIES, default=False, null=False)
    city = models.CharField(max_length=30, null=False, blank=True)
    state = models.CharField(max_length=50, null=False, blank=True)
    zip_code = models.PositiveIntegerField(max_length=10, null=False, default=False)

    def __str__(self):
        return 'Order: ' + str(self.id)

    class Meta:
        ordering = ('timestamp', )


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
