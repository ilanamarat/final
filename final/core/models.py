from django.db import models


from django.conf import settings 
from django.contrib.auth.models import (
	AbstractBaseUser, BaseUserManager, PermissionsMixin
)
# Create your models here.
JOURNAL_TYPE = (
    ('B', 'BULLET'),
    ('F', 'FOOD'),
    ('T', 'TRAVEL'),
    ('S', 'SPORT')
)
ROLES = (
    ('SA', 'SuperAdmin'),
    ('G', 'Guest')
)

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if username is None:
            raise TypeError('Write username')
        if email is None:
            raise TypeError('Enter email')
        
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user
    def create_superuser(self, username, email, password):
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user
    
class UserProfile(AbstractBaseUser,PermissionsMixin):
    username = models.CharField(max_length=200,unique=True, null=True, blank=True )
    email = models.EmailField(max_length=200)
    roles= models.CharField(choices=ROLES, max_length=2, default='G')
    is_staff = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'

    REQUIRED_FIELDS=['email']

    objects = UserManager()

    def __str__(self):
        return self.username

    def get_role(self):
        return self.roles


class BookJournalBase(models.Model):
    name = models.CharField(max_length=200, default='No name')
    price = models.FloatField(default=0)
    description = models.CharField(max_length=500, default='No description')
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        abstract = True
    def __str__(self) -> str:
        return self.name

class Book(BookJournalBase):
    num_pages = models.IntegerField(default=0)
    genre = models.CharField(max_length=100, default='No genre')

    def __str__(self) -> str:
        return super().__str__()

class Journal(BookJournalBase):
    type = models.CharField(choices=JOURNAL_TYPE, default='B', max_length=2)
    publisher = models.CharField(max_length=500)

    def __str__(self) -> str:
        return super().__str__()