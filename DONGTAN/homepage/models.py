from django.db import models
from django.urls import reverse

# Create your models here.

class Menu(models.Model):
	name=models.CharField('NAME',max_length=50)
	price=models.IntegerField('PRICE')
	description=models.TextField('DESCRIPTION',max_length=100, blank=True, help_text='explanation for food')

	class Meta:
		verbose_name='menu'
		verbose_name_plural='menus'
		db_table='dongtanjumak_menu'

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse()
