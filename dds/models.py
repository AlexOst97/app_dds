from django.db import models


class Status(models.Model):
    """Статус (Например: Бизнес, Личное, Налог и т.д.)"""

    name = models.CharField(max_length=100, verbose_name="Название статуса")

    class Meta:
        verbose_name = "Статус"
        verbose_name_plural = "Статусы"

    def __str__(self):
        return f"{self.name}"


class Type(models.Model):
    """Типы операций (Пополнение, Списание и т.д.)"""

    name = models.CharField(max_length=100, verbose_name="Название типа")

    class Meta:
        verbose_name = "Тип операции"
        verbose_name_plural = "Типы операций"

    def __str__(self):
        return f"{self.name}"


class Category(models.Model):
    """Катерогия"""

    name = models.CharField(max_length=100, verbose_name="Название категории")

    description = models.TextField(
        blank=True, null=True, verbose_name="Описание категории"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name}"


class Subcategory(models.Model):
    """Подкатегория для Category (категории)"""

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name="subcategories",
        verbose_name="Категория",
    )
    name = models.CharField(max_length=100, verbose_name="Название подкатегории")

    description = models.TextField(
        blank=True, null=True, verbose_name="Описание подкатегории"
    )

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"

    def __str__(self):
        return f"{self.category.name} - {self.name}"


class CashFlow(models.Model):
    """Движение денежных средств (ДДС)"""

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    status = models.ForeignKey(Status, on_delete=models.PROTECT, verbose_name="Статус")

    type = models.ForeignKey(Type, on_delete=models.PROTECT, verbose_name="Тип")

    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, verbose_name="Категория"
    )

    subcategory = models.ForeignKey(
        Subcategory, on_delete=models.PROTECT, verbose_name="Подкатегория"
    )

    sum = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name="Сумма",
    )

    comment = models.TextField(
        blank=True,
        null=True,
        verbose_name="Комментарий",
    )

    class Meta:
        verbose_name = "Запись движения денежных средств"
        verbose_name_plural = "Записи движения денежных средств"

    def __str__(self):
        return f"{self.id}"
