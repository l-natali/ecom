# Generated by Django 4.1.4 on 2022-12-19 15:20

import base.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('photo', models.ImageField(upload_to=base.models.About.get_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='AboutBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to=base.models.AboutBanner.get_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='AccountBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to=base.models.AccountBanner.get_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='Advantages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, unique=True)),
                ('description', models.CharField(db_index=True, max_length=200, unique=True)),
                ('photo', models.ImageField(upload_to=base.models.Advantages.get_file_name)),
                ('position', models.SmallIntegerField(unique=True)),
            ],
            options={
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='BlogDetailBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to=base.models.BlogDetailBanner.get_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50, unique=True)),
                ('logo', models.ImageField(upload_to=base.models.Brands.get_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='CartBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to=base.models.CartBanner.get_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=50, unique=True)),
                ('position', models.SmallIntegerField(unique=True)),
                ('is_visible', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='CompareBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to=base.models.CompareBanner.get_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(default='info@nelson.com.ua', max_length=50)),
                ('phone', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='ContactBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to=base.models.ContactBanner.get_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='DiscountBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, unique=True)),
                ('photo', models.ImageField(upload_to=base.models.DiscountBanner.get_file_name)),
                ('discount', models.SmallIntegerField(blank=True, max_length=2)),
                ('date', models.CharField(max_length=10)),
            ],
            options={
                'ordering': ('date',),
            },
        ),
        migrations.CreateModel(
            name='Faq',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=100)),
                ('answer', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='FaqBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to=base.models.FaqBanner.get_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='Furniture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, unique=True)),
                ('photo', models.ImageField(upload_to=base.models.Furniture.get_file_name)),
                ('position', models.SmallIntegerField(unique=True)),
            ],
            options={
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='HomeBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=100, unique=True)),
                ('photo', models.ImageField(upload_to=base.models.HomeBanner.get_file_name)),
                ('position', models.SmallIntegerField(unique=True)),
            ],
            options={
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='LoginBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to=base.models.LoginBanner.get_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='ProductDetailBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to=base.models.ProductDetailBanner.get_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to=base.models.ProductPhoto.get_file_name)),
                ('description', models.CharField(blank=True, max_length=20)),
                ('position', models.SmallIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('company', models.CharField(max_length=50)),
                ('avatar', models.ImageField(upload_to=base.models.Review.get_file_name)),
                ('back_photo', models.ImageField(upload_to=base.models.Review.get_file_name)),
                ('review', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='ShopBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to=base.models.ShopBanner.get_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='Subscribe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator(message='Email in format xxxxxx@xx.xx', regex='^[^-_][a-zA-Z0-9_-]+@\\w+\\.\\w+$')])),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-date', '-is_processed'),
            },
        ),
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=50)),
                ('photo', models.ImageField(upload_to=base.models.Team.get_file_name)),
                ('twitter', models.CharField(default='http://', max_length=100)),
                ('instagram', models.CharField(default='http://', max_length=100)),
                ('facebook', models.CharField(default='http://', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='WishlistBanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('photo', models.ImageField(upload_to=base.models.WishlistBanner.get_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='WriteUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=500)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_processed', models.BooleanField(default=False)),
            ],
            options={
                'ordering': ('-date', '-is_processed'),
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=200)),
                ('title', models.CharField(db_index=True, max_length=100, unique=True)),
                ('description_short', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('color', models.CharField(max_length=20)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('sale', models.SmallIntegerField(blank=True, max_length=2)),
                ('new_arrival', models.BooleanField(default=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('featured', models.BooleanField(default=False)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.category')),
                ('photo', models.ManyToManyField(to='base.productphoto')),
            ],
            options={
                'index_together': {('id', 'slug')},
            },
        ),
    ]
