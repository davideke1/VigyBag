from django.shortcuts import render

# Create your views here.
from .models import Item, Category


def index(request):
    headphone_category = Category.objects.get(name='headphones')
    headphones_items = headphone_category.item_set.all()

    clothes_category = Category.objects.get(name='clothes')
    clothes_items = clothes_category.item_set.all()

    context = {
        'myrange': range(5),
        'headphones': headphones_items,
        'clothes':clothes_items,
    }
    return render(request, 'home/index.html', context)


def cart(request):
    return render(request, 'home/cart.html')