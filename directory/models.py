from django.db import models

# Create your models here.
class Listings(models.Model):
	crsid = models.CharField(max_length=8)
	full_name = models.CharField(max_length=30)
	event_name = models.CharField(max_length=50)
	event_date = models.DateField()
	price = models.DecimalField(max_digits = 10000, decimal_places=2)

	@property
	def price_display(self):
		return "£%s" % self._price_display
	

	date_added = models.DateTimeField(auto_now_add = True)
	last_modified = models.DateTimeField(auto_now = True)
	chat = models.TextField()

	EVENT_CHOICES = [
	('May Ball', 'May Ball'),
	('Queer Get Down', 'Queer Get Down'),
	('Wednesday Revs', 'Wednesday Revs'),
	('Sunday Lolas', 'Sunday Lolas'),
	("Captain's Cocktails", "Captain's Cocktails"),
	("Friday Mash", "Friday Mash"),
	("Saturday Mash", "Saturday Mash"),
	("Other", "Other")
	]

	event_type = models.CharField(choices = EVENT_CHOICES, max_length=30)

	def __str__(self):
		return self.full_name
