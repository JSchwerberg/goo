from django.core.cache import cache
from django.core.mail import send_mail
from .models import Sponsor
from .generators import id_generator
import hashlib
import uuid
import os

def check_password(username, password, salt="lk13lkjf8039kjfdklsc1--@jfd", old=False):
    user = Sponsor.objects.get(username=username)

    if old:
        salt = hashlib.md5(salt)
        password = hashlib.md5(password + salt.hexdigest())
        for i in range(9008):
            password = hashlib.md5(password.hexdigest() + salt.hexdigest())
        password = password.hexdigest()
    else:
        password = hashlib.sha256(password + salt).hexdigest()

    if password == user.password:
        return True

    return False

def hash_password(password):
    
    salt = os.urandom(16).encode('base_64')
    password = hashlib.sha256(password + salt).hexdigest()
    return (password, salt)

def check_complexity(s, required=2):
    complexity = 0
    if s.isalnum() and not s.isalpha():
        complexity += 1
    if len(s) > 7:
        complexity += 1
    
    if complexity >= required:
        return True
    return False

def send_reset_email(s):
    """s should be an object of the Sponsor class"""
    
    email = s.email
    username = s.username
    sponsor_id = s.id
    reset_key = id_generator(size=20)

    cache.set('reset_%s' % reset_key, sponsor_id, 86400) 

    message = "We have received a request to reset your password for your "
    message += "Goo.im sponsor account.  Please click the link below to reset your password.\n\n"
    message += "https://goo.im/sponsor/password?token=%s" % reset_key
    message += "\n\n"
    message += "If you feel that you received this message in error, or you did not request a password "
    message += "reset, please contact our admins by replying to this email."
    message += "\n\n"
    message += "-- The Goo.im team"

    send_mail('Password Request', message,
        'support@snipanet.com', [email])

