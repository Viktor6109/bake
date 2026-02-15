from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

from goods.models import Products


# Create your views here.
# def catalog(request, category_slug):
#     page: int = request.GET.get('page', 1)
#     on_sale: bool = request.GET.get('on_sale', None)
#     order_by = request.GET.get('order_by', None)

#     if category_slug == 'all':
#         goods = Products.objects.all()
#     else:
#         goods = Products.objects.filter(category__slug=category_slug)

#     if on_sale:
#         goods = goods.filter(discount__gt=0)

#     if order_by and order_by != "default":
#         goods=goods.order_by(order_by)

#     paginator = Paginator(goods, 3)
#     current_page = paginator.get_page(page)

#     context = {
#         'title': 'Продукция',
#         'goods': current_page,
#         'slug_url': category_slug,
#     }


#     return render(request, 'goods/catalog.html', context)
def catalog(request, category_slug):
    if category_slug == "all":
        goods = Products.objects.all()
    else:
        goods = Products.objects.filter(category__slug=category_slug)

    # Применяем фильтры и сортировку
    on_sale = request.GET.get("on_sale")
    if on_sale == "on":
        goods = goods.filter(discount__gt=0)

    order_by = request.GET.get("order_by", "default")
    if order_by == "price":
        goods = goods.order_by("price")
    elif order_by == "-price":
        goods = goods.order_by("-price")
    # Пагинация
    page = request.GET.get("page", 1)
    paginator = Paginator(goods, 3)

    # Безопасное преобразование page в число
    try:
        page_num = int(page)
    except (ValueError, TypeError):
        page_num = 1

    if page_num < 1:
        page_num = 1

    current_page = paginator.get_page(page_num)

    # Сериализуем GET-параметры, исключая page, чтобы сохранить фильтры при переходе
    params = request.GET.copy()
    params.pop("page", None)
    params = params.urlencode()

    context = {
        "title": "Продукция",
        "goods": current_page,
        "slug_url": category_slug,
        "params": params,
    }

    return render(request, "goods/catalog.html", context)


def product(request, product_slug):
    product = Products.objects.get(slug=product_slug)
    context = {
        "product": product,
    }
    return render(request, "goods/product.html", context)
