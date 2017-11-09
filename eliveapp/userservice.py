from django.contrib.auth.models import User
from eliveapp.models import Channel
from eliveapp.hashutils import HashUtils
import re, reprlib, logging

class UserService:
    def __init__(self):
        self.logger = logging.getLogger('elive')

    def create_user(self, login, mail, password):
        is_valid = self.validate_new_user(login,mail)
        if is_valid:
            self.logger.debug("Creation du user " + login + ", " + mail)
            new_user = User.objects.create_user(login.lower(),mail,password)
            new_channel = Channel(title=login.lower(),topic="",key=HashUtils.random_channel_key())
            new_user.save()
            new_channel.save()
        else:
            self.logger.error("User invalide ??")

    def validate_new_user(self,login,mail):
        is_valid = False
        #authorized characters
        login_re = re.compile("\w+")
        is_valid = login_re.match(login)

        if not is_valid:
            raise CreateUserException("login invalide : " + login)

        if is_valid:
            #username not already taken
            is_valid = not User.objects.filter(username=login.lower()).exists()

        if not is_valid:
            raise CreateUserException("utilisateur déjà existant : " + login)

        if is_valid:
            #mail not already taken
            is_valid = not User.objects.filter(email=mail).exists()

        if not is_valid:
            raise CreateUserException("mail déjà existant : " + mail)
        return is_valid

class CreateUserException(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
