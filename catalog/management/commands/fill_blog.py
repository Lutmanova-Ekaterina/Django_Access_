from django.core.management import BaseCommand
from catalog.models import Blog
import datetime


class Command(BaseCommand):

    def handle(self, *args, **options):
        blogs = [
            {'head': 'cake', 'slug': 'cake',
             'content': 'a little sweet cake', 'image': 'cake.jpg',
             'date_create': datetime.date.today()},
            {'head': 'milkshake', 'slug': 'cake',
             'content': 'a chocolate, a strawberry, a banana milkshake', 'image': 'milkshake.jpg',
             'date_create': datetime.date.today()}
        ]

        blogs_list = []

        for item in blogs:
            blogs_list.append(Blog(**item))

        Blog.objects.all().delete()
        Blog.objects.bulk_create(blogs_list)
