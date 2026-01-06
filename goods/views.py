from django.shortcuts import render

# Create your views here.
def catalog(request):
    context = {
      'title': 'Продукция',
      'content': 'Перечень продукции'
    }
    return render(request, 'goods/catalog.html', context)


def product(request):
    context = {
        'title': 'Продукт',
        'content': 'Карточка продукта'
    }
    return render(request, 'goods/product.html', context)


