from django.db import models


class DisplayModel(models.Model):
    name = models.CharField(verbose_name="Название экрана", max_length=64)

    class Meta:
        verbose_name = 'Экран'
        verbose_name_plural = 'Экраны'

    def __str__(self):
        return f'{self.name}'


class HeaderModel(models.Model):
    display = models.ForeignKey(DisplayModel, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название", max_length=64)
    text = models.TextField(verbose_name='Текст заголовка')

    class Meta:
        verbose_name = 'Заголовок'
        verbose_name_plural = 'Заголовки'

    def __str__(self):
        return f"{self.name}"


class TextModel(models.Model):
    display = models.ForeignKey(DisplayModel, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название", max_length=64)
    text = models.TextField(verbose_name='Текст моделей')

    class Meta:
        verbose_name = 'Текст'
        verbose_name_plural = 'Текста'

    def __str__(self):
        return f"{self.name}"


class ImageModel(models.Model):
    name = models.CharField(verbose_name="Название", max_length=64)
    display = models.ForeignKey(DisplayModel, on_delete=models.CASCADE)
    media_image = models.ImageField(upload_to='images/')
    alt = models.TextField(verbose_name='alt', null=True)
    title = models.TextField(verbose_name='title', null=True)

    class Meta:
        verbose_name = 'Картинка'
        verbose_name_plural = 'Картинки'

    def __str__(self):
        return f"{self.name}-{self.alt}-{self.title}"

    def to_dict(self):
        return {
            'media_image': self.media_image,
            'alt': self.alt,
            'title': self.title
        }


class LinkModel(models.Model):
    display = models.ForeignKey(DisplayModel, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название", max_length=64)
    text = models.TextField(verbose_name="Текст")
    href = models.TextField(verbose_name="Ссылка")
    title = models.TextField(verbose_name="title", blank=True, null=True)

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'

    def __str__(self):
        return f"{self.name}"


class ButtonModel(models.Model):
    display = models.ForeignKey(DisplayModel, on_delete=models.CASCADE)
    name = models.CharField(verbose_name="Название", max_length=64)
    visible = models.BooleanField(verbose_name='Показывать', blank=True, null=True)
    text = models.TextField(verbose_name="Текст")
    href = models.TextField(verbose_name="Ссылка")
    title = models.TextField(verbose_name="title", blank=True, null=True)
    add_form = models.BooleanField(verbose_name='Форма номер 2')

    class Meta:
        verbose_name = 'Кнопка'
        verbose_name_plural = 'Кнопки'

    def __str__(self):
        return f"{self.name}"


class CardModel(models.Model):
    name = models.CharField(verbose_name='Название', max_length=64)
    visible = models.BooleanField(verbose_name='Показать')
    title = models.CharField(verbose_name='Заголовок карточки', max_length=64)
    subtitle = models.CharField(verbose_name='Подзаголовок карточки', max_length=64)
    price = models.CharField(verbose_name='Цена', max_length= 64)
    descr = models.TextField(verbose_name='Характеристики товара')
    href = models.TextField(verbose_name="Ссылка")

    class Meta:
        verbose_name = 'Карточка'
        verbose_name_plural = 'Карточки'

    def __str__(self):
        return f"{self.name} - {self.title}"

    def to_dict(self):
        return {
            'name': self.name,
            'visible': self.visible,
            'title': self.title,
            'subtitle': self.subtitle,
            'price': self.price,
            'descr': self.descr.split(','),
            'href': self.href
        }


class FormModel(models.Model):
    name = models.CharField(verbose_name='Название формы', max_length=64)
    mail_to = models.CharField(verbose_name='Почта куда отправлять данные пользователей', max_length=128)

    class Meta:
        verbose_name = 'Форма'
        verbose_name_plural = 'Формы'

    def __str__(self):
        return f"{self.name}"


class IconModel(models.Model):
    name = models.CharField(verbose_name='Название иконки', max_length=64)
    href = models.TextField(verbose_name="Ссылка")
    icon = models.CharField(verbose_name='Название иконки из font-awesome', max_length=64)

    class Meta:
        verbose_name = 'Иконка'
        verbose_name_plural = 'Иконки'

    def __str__(self):
        return f"{self.name}"


class NewsModel(models.Model):
    name = models.CharField(verbose_name='Название новости', max_length=64)
    href = models.TextField(verbose_name="Ссылка")
    date = models.CharField(verbose_name='Дата публикации новости', max_length=64)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return f"{self.name}"
