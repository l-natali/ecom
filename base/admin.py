from django.contrib import admin
from .models import Category, Product, ProductPhoto, HomeBanner, Furniture, DiscountBanner, Advantages, Review, Brands
from .models import Contact, Subscribe, WriteUs, AboutBanner, About, Team, FaqBanner, Faq, ShopBanner
from .models import ContactBanner, ProductDetailBanner, CompareBanner, WishlistBanner, BlogDetailBanner
from .models import AccountBanner, LoginBanner, CartBanner


admin.site.register(Category)
admin.site.register(HomeBanner)
admin.site.register(Furniture)
admin.site.register(DiscountBanner)
admin.site.register(Advantages)
admin.site.register(Review)
admin.site.register(Brands)
admin.site.register(Contact)
admin.site.register(Subscribe)
admin.site.register(WriteUs)
admin.site.register(About)
admin.site.register(AboutBanner)
admin.site.register(Team)
admin.site.register(Faq)
admin.site.register(FaqBanner)
admin.site.register(ContactBanner)
admin.site.register(ShopBanner)
admin.site.register(ProductDetailBanner)
admin.site.register(CompareBanner)
admin.site.register(WishlistBanner)
admin.site.register(BlogDetailBanner)
admin.site.register(AccountBanner)
admin.site.register(LoginBanner)
admin.site.register(CartBanner)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_filter = ('category', )
    prepopulated_fields = {'slug': ('title', ), }


@admin.register(ProductPhoto)
class ProductPhotoAdmin(admin.ModelAdmin):
    list_filter = ('product', )

