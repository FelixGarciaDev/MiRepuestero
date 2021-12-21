from django.db import models

from users.models import User


# Create your models here.
class Client(models.Model):
    #Basic client user information and flags
    user 			= models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firts_login     = models.BooleanField(default=True)    
    profile_pic     = models.ImageField(upload_to='Client_Media/Imagen_Perfil/', 
                                                default='Client_Media/Imagen_Perfil/user_default_profilepic.png')
    name            = models.CharField(max_length=50)    
    last_name       = models.CharField(max_length=50)   
    id_number       = models.IntegerField(null=False, default=0)
    phone1          = models.IntegerField(null=False, default=0)
    phone2          = models.IntegerField(default=0)