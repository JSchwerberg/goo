from django.db import models
from django.contrib.auth.models import User
from paypal.standard.ipn

class Sponsor(models.Model):
	user = models.OneToOneField(User)
	payment_id = models.CharField(max_length=32,blank=True,null=True,default=None)

	def activate_sponsor(self, tx_id="DEVELOPER"):
		u = self.user
		u.is_active = True
		self.payment_id = tx_id

	def deactivate_sponsor(self):
		u.is_active = False