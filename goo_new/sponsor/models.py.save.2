from django.db import models
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.utils.translation import ugettext as _
from paypal.standard.ipn.signals import payment_was_successful, \
          payment_was_flagged, payment_was_refunded, \
          payment_was_reversed
from .generators import id_generator


class Sponsor(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=64)
    created = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)
    salt = models.CharField(max_length=64)
    payment_id = models.CharField(max_length=32, default="DEVELOPER")
    email = models.CharField(max_length=100)
    migrated = models.BooleanField(default=True)

    def activate_sponsor(self, txn_id):
        self.status = True
        self.payment_id = txn_id

    def deactivate_sponsor(self):
        self.status = False


    class Meta:
        verbose_name = _('Sponsor')
        verbose_name_plural = _('Sponsors')

    def __unicode__(self):
        return u'%s' % self.username

class AuthKey(models.Model):
    token = models.CharField(max_length=12)
    payment_id = models.CharField(max_length=32)
    email = models.CharField(max_length=50)

    def __unicode__(self):
        return u'%s' % self.email

def successful_payment(sender, **kwargs):
    ipn_obj = sender

    email = ipn_obj.payer_email
    item = ipn_obj.item_name
    gross = ipn_obj.mc_gross

    if item == "Goo.IM Sponsor Account" and gross == 10.00:

        key = AuthKey(token=id_generator(), payment_id=ipn_obj.txn_id, email=email)
        key.save()
        message = "Your payment for your sponsor signup has been processed, "
        message += "and your key is:\n\n"
        message += key.token + "\n\n"
        message += "You can finish your signup by following this link:\n\n"
        message += '<a href="https://goo.im/sponsor/auth/?token=%s">https://goo.im/sponsor/auth/?token=%s\n\n</a>' % (key.token, key.token)
        message += "If this link doesn't work for you, you can visit " 
        message += "https://goo.im/sponsor_signup and enter the key manually.\n\n"
        message += "Thanks for supporting Goo.im!\n\n"
        message += "-- The Goo.im team"
        send_mail('Finish your sponsor signup', message,
			'support@snipanet.com', [email])

payment_was_successful.connect(successful_payment)

def flagged_payment(sender, **kwargs):
	ipn_obj = sender

	email = ipn_obj.payer_email

	message = "Your payment for your Goo.im sponsor signup has been held "
	message += "for manual processing.  Our admins will look into the issue, "
	message += "and contact you if we need additional information.  We "
	message += "apologize for the delay, and will take care of this as soon "
	message += "as possible.\n\n"
	message += "-- The Goo.im team"
	send_mail('Your sponsor signup has been delayed', message,
		'support@snipanet.com', [email])

	admin_message = "A paypal payment has been flagged with the following "
	admin_message += "error: %s\n\n" % ipn_obj.flag
	admin_message += "Transaction ID: %s\n" % ipn_obj.txn_id
	admin_message += "Email Address: %s\n" % ipn_obj.payer_email
	send_mail('Flagged Payment', message,
		'support@snipanet.com', ['errors@snipanet.com'])

# payment_was_flagged.connect(flagged_payment)

def refunded_payment(sender, **kwargs):

    ipn_obj =sender

    txn_id = ipn_obj.parent_txn_id

    try:
        AuthKey.objects.get(payment_id=txn_id).delete()
    except:
        pass

    try:
        sponsor = Sponsor.objects.get(payment_id=txn_id)
    except:
        pass
    else:
        sponsor.status = False

payment_was_refunded.connect(refunded_payment)

def reversed_payment(sender, **kwargs):

    ipn_obj =sender

    txn_id = ipn_obj.parent_txn_id
    email = ipn_obj.payer_email

    try:
        AuthKey.objects.get(payment_id=txn_id).delete()
    except:
        pass

    try:
        sponsor = Sponsor.objects.get(payment_id=txn_id)
    except:
        pass
    else:
        sponsor.status = False

    message = "We have received notification that your paypal transaction "
    message += "for your Goo.im sponsor account has been reversed. "
    message += "We have therefore removed your sponsor access to the site, and any authentication "
    message += "keys that we have for your account have been invalidated.\n\n"
    message += "If you feel that you received this message in error, please contact our admins "
    message += "by replying to this email."
    message += "\n\n"
    message += "-- The Goo.im team"

    send_mail('Payment Chargedback', message,
        'support@snipanet.com', [email])



payment_was_reversed.connect(reversed_payment)

