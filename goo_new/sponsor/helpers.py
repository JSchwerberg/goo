from .models import Sponsor
import hashlib

def check_password(username, password, salt="lk13lkjf8039kjfdklsc1--@jfd", old=False):
    user = Sponsor.objects.get(username=username)

    if old:
        salt = hashlib.md5(salt)
        password = hashlib.md5(password + salt.hexdigest())
        for i in range(9008):
            password = hashlib.md5(password.hexdigest() + salt.hexdigest())
        password = password.hexdigest()
    else:
        password = hashlib.sha256(password + salt.hexdigest())

    if password == user.password:
        return True

    return False
