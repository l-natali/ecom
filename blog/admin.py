from django.contrib import admin


from .models import Blog, BlogBanner

admin.site.register(BlogBanner)


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', ), }
