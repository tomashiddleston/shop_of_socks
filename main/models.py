from django.db import models


class Task(models.Model):
    title = models.CharField('Название', max_length=50)
    task = models.TextField('Описание')
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'

class Product(models.Model):
	product_id = models.CharField('Номер товара', max_length=5)
	product_name = models.CharField('Название товара', max_length=100)
	product_price = models.FloatField('Закупочная цена', max_length=10)
	product_size = models.CharField('Размер', max_length=15)
	product_count = models.CharField('Доступность', max_length=3, default=0)
	product_image = models.ImageField(upload_to='photos/%Y/%m/%d/')
	uploaded_at = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.product_name

	class Meta:
		verbose_name = 'Товар'
		verbose_name_plural = 'Товары'

class Order(models.Model):
	order_id = models.CharField('Номер заказа', max_length=10)
	order_name = models.CharField('ФИО покупателя', max_length=50)
	order_address = models.CharField('Адрес покупателя', max_length=100)
	order_contain = models.CharField('Содержимое заказа', max_length=100)
	order_status = models.CharField('Статус заказа', max_length=100)

	def __str__(self):
		return self.order_name
    
	class Meta:
		verbose_name = 'Заказ'
		verbose_name_plural = 'Заказы'


