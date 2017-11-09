import base64
from django.contrib.auth.hashers import make_password
from os import urandom
from math import floor
import time
import random
import string

class HashUtils:
    default_algorithm = 'pbkdf2_sha256'

    def compare_keys(key,raw_key):
        #$algorithm$iterations$salt$hash
        key_split = key.split('$');
        algorithm = key_split[0];
        salt = key_split[2];
        inputkey_hashed = make_password(password=raw_key,salt=salt,hasher=algorithm)
        return inputkey_hashed == key
    @classmethod
    def hash(cls,raw_key):
        return make_password(password=raw_key,hasher=cls.default_algorithm)
    @classmethod
    def random_channel_key(cls):
        epoch = floor(time.time()) + random.randint(3600, 2592000)
        key = base64.b64encode(urandom(32)).decode('utf-8').translate(str.maketrans("+/=","-_,"))+"_"+str(epoch)
        return key
