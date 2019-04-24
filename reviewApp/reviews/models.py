from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
	name = models.CharField(default = '', max_length = 255)
	brand = models.CharField(default = '',max_length = 255)
	avg_cost = models.DecimalField(default = 00.00, max_digits = 5, decimal_places = 2)
	category = models.CharField(default = '', max_length = 255)
	date_released = models.DateField(default = timezone.now)
	description = models.TextField()
	photo = models.ImageField(default = 'default.jpg', upload_to = 'product_pics')

	def __str__(self):
		return self.name

class Review(models.Model):
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	products = models.ForeignKey(Product, on_delete = models.CASCADE)
	rating = models.IntegerField(default = 0, max_length = 5)
	review_text = models.TextField()
	date = models.DateField(default = timezone.now)

	def __str__(self):
		return self.author.username

# Create your models here.
