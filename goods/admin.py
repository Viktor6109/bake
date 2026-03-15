from django.contrib import admin

from goods.models import Categories, Products

# admin.site.register(Categories)
# admin.site.register(Products)


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    # Добавляем отображение ID и других полей в списке
    list_display = ("display_id", "name", "price", "discount", "category")
    list_filter = ("category", "discount")
    search_fields = ("name", "description")


# Register your model
