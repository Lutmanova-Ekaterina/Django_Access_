from django.core.management import BaseCommand
from catalog.models import Product, Category
import datetime


class Command(BaseCommand):
    def handle(self, *args, **options):
        products = [
            {'product_name': 'cake',
             'title': 'Cake is a flour confection made from flour, sugar, and other ingredients, and is usually baked. In their oldest forms, cakes were modifications of bread, but cakes now cover a wide range of preparations that can be simple or elaborate, and which share features with desserts such as pastries, meringues, custards, and pies. The most common ingredients include flour, sugar, eggs, fat (such as butter, oil or margarine), a liquid, and a leavening agent, such as baking soda or baking powder.',
             'category': 1, 'image': 'cake.jpg', 'price': '200',
             'date_create': datetime.date.today(),
             'date_update': datetime.date.today()},
            {'product_name': 'milkshake',
             'title': 'A milkshake (sometimes called a shake in the United States) is a sweet drink made by blending milk, ice cream, and flavorings or sweeteners such as butterscotch, caramel sauce, chocolate syrup, fruit syrup, or whole fruit into a thick, sweet, cold mixture. It may also be made using other types of milk such as almond milk, coconut milk, or soy milk.',
             'category': 2, 'image': 'milkshake.jpg', 'price': '30',
             'date_create': datetime.date.today(),
             'date_update': datetime.date.today()},
        ]

        categories = [
            {'category_name': 'desserts', 'title': 'yummy, sweet'},
            {'category_name': 'drinks', 'title': 'quench your thirst'},
            {'category_name': 'sundae', 'title': 'dairy, cools on a hot days'},
        ]

        products_list = []
        categories_list = []

        for item in categories:
            categories_list.append(Category(**item))

        Category.objects.all().delete()
        Category.objects.bulk_create(categories_list)

        for item in products:
            products_list.append(Product(**item))
            
        Product.objects.all().delete()
        Product.objects.bulk_create(products_list)
