from django.db import models
from django.core.validators import RegexValidator
import uuid
import os.path
from django.urls import reverse


class Category(models.Model):

    title = models.CharField(unique=True, max_length=50, db_index=True)
    position = models.SmallIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position', )


class ProductPhoto(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('product_photo/', new_filename)

    photo = models.ImageField(upload_to=get_file_name)
    description = models.CharField(max_length=20, blank=True)
    position = models.SmallIntegerField(default=1)

    def __str__(self):
        return f'{self.description}'


class Product(models.Model):

    slug = models.SlugField(max_length=200, db_index=True)
    title = models.CharField(unique=True, max_length=100, db_index=True)
    description_short = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    color = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    sale = models.SmallIntegerField(max_length=2, blank=True)
    new_arrival = models.BooleanField(default=True)
    is_visible = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    photo = models.ManyToManyField(ProductPhoto)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        index_together = (('id', 'slug'), )

    def get_absolute_url(self):
        return reverse("shop:products", args=[self.slug])


class HomeBanner(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('homebanner/', new_filename)

    title = models.CharField(unique=True, max_length=100, db_index=True)
    photo = models.ImageField(upload_to=get_file_name)
    position = models.SmallIntegerField(unique=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position', )


class Furniture(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('photo/', new_filename)

    title = models.CharField(unique=True, max_length=100, db_index=True)
    photo = models.ImageField(upload_to=get_file_name)
    position = models.SmallIntegerField(unique=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position', )


class DiscountBanner(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('discban/', new_filename)

    title = models.CharField(unique=True, max_length=100, db_index=True)
    photo = models.ImageField(upload_to=get_file_name)
    discount = models.SmallIntegerField(max_length=2, blank=True)
    date = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.title}, {self.date}'

    class Meta:
        ordering = ('date', )


class Advantages(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('advant/', new_filename)

    title = models.CharField(unique=True, max_length=50, db_index=True)
    description = models.CharField(unique=True, max_length=200, db_index=True)
    photo = models.ImageField(upload_to=get_file_name)
    position = models.SmallIntegerField(unique=True)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('position', )


class Review(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('review/', new_filename)

    name = models.CharField(unique=True, max_length=50)
    company = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to=get_file_name)
    back_photo = models.ImageField(upload_to=get_file_name)
    review = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.name}, {self.company}'


class Brands(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('brands/', new_filename)

    company = models.CharField(unique=True, max_length=50)
    logo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.company}'


class Contact(models.Model):

    address = models.CharField(max_length=100)
    email = models.CharField(max_length=50, default='info@nelson.com.ua')
    phone = models.CharField(max_length=12)

    def __str__(self):
        return f'{self.address}, {self.email}, {self.phone}'


class Subscribe(models.Model):

    email_re = RegexValidator(regex=r'^[^-_][a-zA-Z0-9_-]+@\w+\.\w+$', message='Email in format xxxxxx@xx.xx')
    email = models.CharField(max_length=50, validators=[email_re])
    date = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date', '-is_processed')

    def __str__(self):
        return f'{self.email}'


class WriteUs(models.Model):

    email = models.EmailField(max_length=50)
    name = models.CharField(max_length=50)
    message = models.CharField(max_length=500)
    date = models.DateTimeField(auto_now_add=True)
    is_processed = models.BooleanField(default=False)

    class Meta:
        ordering = ('-date', '-is_processed')

    def __str__(self):
        return f'{self.name, self.message[:50]}'


class AboutBanner(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('about_banner/', new_filename)

    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.title}'


class About(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('about/', new_filename)

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.title}'


class Team(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('team/', new_filename)

    name = models.CharField(max_length=50, db_index=True)
    photo = models.ImageField(upload_to=get_file_name)
    twitter = models.CharField(max_length=100, default='http://')
    instagram = models.CharField(max_length=100, default='http://')
    facebook = models.CharField(max_length=100, default='http://')

    def __str__(self):
        return f'{self.name}'


class FaqBanner(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('faq_banner/', new_filename)

    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.title}'


class Faq(models.Model):

    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.question}'


class ContactBanner(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('contact_banner/', new_filename)

    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.title}'


class ShopBanner(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('shop_banner/', new_filename)

    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.title}'


class ProductDetailBanner(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('product_detail_banner/', new_filename)

    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.title}'


class CompareBanner(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('compare_banner/', new_filename)

    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.title}'


class WishlistBanner(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('wishlist_banner/', new_filename)

    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.title}'


class BlogDetailBanner(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('blog_detail_banner/', new_filename)

    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.title}'


class AccountBanner(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('account_banner/', new_filename)

    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.title}'


class LoginBanner(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('login_banner/', new_filename)

    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.title}'


class CartBanner(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('cart_banner/', new_filename)

    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.title}'

