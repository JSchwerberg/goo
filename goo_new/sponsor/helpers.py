from .models import Sponsor
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
