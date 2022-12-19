from django.db import models
from django.urls import reverse
import uuid
import os.path


class Blog(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('blog/', new_filename)

    title = models.CharField(max_length=100, db_index=True)
    photo = models.ImageField(upload_to=get_file_name)
    data = models.DateField(auto_now_add=True)
    slug = models.SlugField(max_length=200, db_index=True)
    text = models.TextField(max_length=5000, default='Input text')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        ordering = ('-data', )
        index_together = (('id', 'slug'), )

    def get_absolute_url(self):
        return reverse("blog:posts", args=[self.slug])


class BlogBanner(models.Model):

    def get_file_name(self, filename: str) -> str:
        ext_file = filename.strip().split('.')[-1]
        new_filename = f'{uuid.uuid4()}.{ext_file}'
        return os.path.join('blog_banner/', new_filename)

    title = models.CharField(max_length=20)
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f'{self.title}'
