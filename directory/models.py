from django.db import models

# Create your models here.
class Doctor(models.Model):
	doc_forename = models.CharField(max_length=30)
	doc_surname = models.CharField(max_length=30)
	doc_info = models.TextField

	INSURANCE_CHOICES = [
	('Cigna', 'Cigna'),
	('BUPA', 'BUPA'),
	('Aviva', 'Aviva'),
	('Cignet', 'Cignet'),
	('Vitality', 'Vitality'),
	('WPA', 'WPA'),
	]

	doc_insurance = models.CharField(choices=INSURANCE_CHOICES, max_length=100)

	def __str__(self):
		return self.doc_surname

class Specialties(models.Model):

	CONDITION_CHOICES = [
	('Depression', 'Depression'),
	('OCD', 'OCD'),
	('Anxiety', 'Anxiety'),
	('PTSD', 'PTSD'),
	('Schizophrenia', 'Schizophrenia'),
	('Bulimia', 'Bulimia'),
	('Bipolar_disorder', 'Bipolar disorder'),
	('BPD', 'BPD'),
	('Postpartum_depression', 'Postpartum depression'),
	]

	condition = models.CharField(choices=CONDITION_CHOICES, max_length=100)
	doctors = models.ManyToManyField(Doctor)

	def __str__(self):
		return self.condition