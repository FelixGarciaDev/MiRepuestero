from django.db import models

from users.models import User

#DICCIONARIOS para opciones multiples
CATEGORIAS = (
    ('1', 'Bikes'),
    ('2', 'Cars'),
    ('3', 'Trucks'),
)

RIF_TYPE = (
    ('1', 'V'),#Firmas Personales
    ('2', 'J'),#Personas Juridicas
    ('3', 'E'),#extranjeros
    ('4', 'P'),#pasaporte
    ('5', 'G'),#Gobierno
)

MEMBERSHIP = (
    ('0', 'none'),
    ('1', 'Local'),
    ('2', 'expert'),
    ('3', 'unlimeted'),
)

class Seller(models.Model):
    #Basic repuestero user information and flags
    user 					    = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    firts_login                 = models.BooleanField(default=True)
    VerifyID_1                  = models.BooleanField(default=False)
    VerifyID_2                  = models.BooleanField(default=False)
    use_dolar                   = models.BooleanField(default=False)
    #Repuestero user data
    logo                        = models.ImageField(upload_to='Repuestero_Media/logos', 
                                                default='Repuestero_Media/logos/default-logo-repuestero.jpg')
    facade_photo                = models.ImageField(upload_to='Repuestero_Media/fachadas/',
                                                default='Repuestero_Media/fachadas/default-fachada-repuestero.jpg')
    name                        = models.CharField(max_length=50)    
    phone1                      = models.IntegerField(null=False, default=0)
    phone2                      = models.IntegerField(default=0)    
    representative_name         = models.CharField(max_length=50)
    representative_name         = models.CharField(max_length=50)
    representative_id_number    = models.IntegerField(null=False, default=0)
    representative_phone        = models.IntegerField(null=False, default=0)
    representative_mail         = models.EmailField()
    #UBICACIONGOOGLEMAPS
    #repuestero legal data    
    rif_type                    = models.CharField(max_length=1, choices=RIF_TYPE, default='2')
    rif                         = models.IntegerField(null=False, default=0)
    rif_scan                    = models.ImageField(upload_to='Repuestero_Media/legales', 
                                                null=True)
    #repuestero payment data
    membership_type             = models.CharField(max_length=1, choices=MEMBERSHIP, default='0')    
    voucher_scan                = models.ImageField(upload_to='Repuestero_Media/pagos', 
                                                null=True)
    voucher_sended              = models.BooleanField(default=False)
    voucher_checked             = models.BooleanField(default=False)
    #Repuestero dolar data
    uses_bcv                    = models.BooleanField(default=False)
    dolar_value                 = models.IntegerField(null=False, default=1)
    #Asi se si el repuestero es favorito y de quien
    favorite_seller             = models.ManyToManyField(User, related_name = 'favorite_refiller', default = False)

class Publication(models.Model):
    owner               = models.ForeignKey(User, on_delete=models.CASCADE, related_name='publications')
    category            = models.CharField(max_length=1, choices=CATEGORIAS, default='1')
    name                = models.CharField(null=False, max_length=500)
    part_number         = models.CharField(max_length=280)
    price               = models.FloatField(null=False, default=0)
    active              = models.BooleanField(default=False)
    aka                 = models.CharField(max_length=280)
    works_for           = models.CharField(max_length=280)
    description         = models.CharField(max_length=5000)
    image               = models.FileField(upload_to='Repuestero_Media/publicaciones/carros/', default='spareParts.png')
    image2              = models.FileField(upload_to='Repuestero_Media/publicaciones/carros/', default='Repuestero_Media/publicaciones/carros/DefaultPart.jpg')
    image3              = models.FileField(upload_to='Repuestero_Media/publicaciones/carros/', default='Repuestero_Media/publicaciones/carros/DefaultPart.jpg')
    image4              = models.FileField(upload_to='Repuestero_Media/publicaciones/carros/', default='Repuestero_Media/publicaciones/carros/DefaultPart.jpg')
    image5              = models.FileField(upload_to='Repuestero_Media/publicaciones/carros/', default='Repuestero_Media/publicaciones/carros/DefaultPart.jpg')
    #ASI si es una publicación favorita y de quien
    favorite_of         = models.ManyToManyField(User, related_name = 'favorite_part', default = False)
