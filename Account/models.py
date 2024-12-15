from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
import random
# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, email,username, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have username")
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, username,password):
         user = self.create_user(
            email = self.normalize_email(email),
            username=username,
            password = password,
        )
         user.is_admin = True
         user.is_staff = True
         user.is_superuser = True
         user.save(using=self._db)
         return user

class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="Email", max_length=60, unique=True)
    username = models.CharField(max_length=60, unique=True)
    img_list = ["pic1","pic2","pic3","pic4","pic5","pic6","pic7","pic8","pic9"]
    img = random.choice(img_list)
    user_image = models.CharField(max_length=255, default=f"accounts/profiles/{img}.jpg", blank=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    
    objects = MyAccountManager()

    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True
    