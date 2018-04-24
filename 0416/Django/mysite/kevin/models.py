from django.db import models

# Create your models here.
class Company(models.Model):
	name = models.CharField(max_length=20)
	adress = models.CharField(max_length=20)

	def __str__(self):
		return self.name

class Employee(models.Model):
	name = models.CharField(max_length=20)
	birthday = models.CharField(max_length=20)
	sexuality = models.CharField(max_length=20)
	company_id = models.ForeignKey(Company)

	def __str__(self):
		return self.name