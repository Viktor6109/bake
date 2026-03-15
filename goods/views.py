from django.core.paginator import Paginator
from django.shortcuts import render

from goods.models import Products


def catalog(request, category_slug):
    if category_slug == "all":
        goods = Products.objects.all().select_related("category")
    else:
        goods = Products.objects.filter(category__slug=category_slug).select_related(
            "category"
        )

    # Применяем фильтры и сортировку
    on_sale = request.GET.get("on_sale")
    if on_sale == "on":
        goods = goods.filter(discount__gt=0)

    order_by = request.GET.get("order_by", "default")
    if order_by == "price":
        goods = goods.order_by("price")
    elif order_by == "-price":
        goods = goods.order_by("-price")
    else:
        goods = goods.order_by("id")  # Сортировка по умолчанию (по id)

    # Пагинация
    page = request.GET.get("page", 1)
    paginator = Paginator(goods, 3)
    current_page = paginator.get_page(page)

    # Сохраняем остальные параметры для пагинации
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
