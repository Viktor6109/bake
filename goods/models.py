from django.db import models


class Categories(models.Model):
    name = models.CharField(unique = True, null = False, blank = False, max_length = 150,
                            verbose_name = 'Название')
    slug = models.SlugField(max_length = 200, unique = True, blank = True, null = True, verbose_name = 'URL')

    class Meta:
        db_table = 'category'
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории'
        ordering = ['name']
        # indexes = [
        #     models.Index(fields = ['category']),
        # ]

    def __str__(self):
        return self.name


class Products(models.Model):
    category = models.ForeignKey(to = Categories, on_delete = models.PROTECT, verbose_name = 'Выбрать категорию',
                                 related_name = 'dessert')
    name = models.CharField(blank = True, max_length = 150, verbose_name = 'Название')
    slug = models.SlugField(max_length = 200, unique = True, blank = True, null = True, verbose_name = 'slug')
    description = models.TextField(blank = True, null = True, verbose_name = 'Описание')
    image = models.ImageField(upload_to = 'goods.image', blank = True, null = True, verbose_name = 'Фотография')

    class Meta:
        db_table = 'products'
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
        ordering = ['category', 'name']

    def __str__(self):
        return self.name

# Create your models here.
