from django.db import models


class Post(models.Model):
    # Данные поста
    title = models.CharField('Заголовок записи', max_length=50)
    descriptions = models.TextField('Текст записи')
    author = models.CharField('Имя автора', max_length=25)
    date = models.DateTimeField('Дата публикации')
    img = models.ImageField('Изображения', upload_to='images/%Y')

    def __str__(self):
        return f'{self.title}, {self.author}'

    class Meta:
        verbose_name = 'Запись'
        verbose_name_plural = 'Записи'


class Comments(models.Model):
    #Коментарий
    email = models.EmailField()
    name = models.CharField('Имя', max_length=50)
    text_comments = models.TextField('Текст коментария', max_length=200)
    post = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name}, {self.post}'

    class Meta:
        verbose_name = 'Коментарий'
        verbose_name_plural = 'Коментарии'


class Liks(models.Model):
    ip = models.CharField('IP-адрес', max_length=60)
    pos = models.ForeignKey(Post, verbose_name='Публикация', on_delete=models.CASCADE)