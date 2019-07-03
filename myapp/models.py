from django.db import models

# Create your models here.
ITEM_CHOICES = [
    (1, 'ubrania, które nadają się do ponownego użycia'),
    (2, 'ubrania do wyrzucenia'),
    (3, 'zabawki'),
    (4, 'książki'),
    (5, 'inne'),
]

LOCATION_CHOICES = [
    (1, 'dolnośląskie'),
    (2, 'kujawsko-pomorskie'),
    (3, 'lubelskie'),
    (4, 'lubuskie'),
    (5, 'łódzkie'),
    (6, 'małopolskie'),
    (7, 'mazowieckie'),
    (8, 'opolskie'),
    (9, 'podkarpackie'),
    (10, 'podlaskie'),
    (11, 'pomorskie'),
    (12, 'śląskie'),
    (13, 'świętokrzyskie'),
    (14, 'warmińsko-mazurskie'),
    (15, 'wielkopolskie'),
    (16, 'zachodniopomorskie'),
]

BENEFICIARY_CHOICES = [
    (1, 'dzieciom'),
    (2, 'samotnym matkom'),
    (3, 'bezdomnym'),
    (4, 'niepełnosprawnym'),
    (5, 'osobom starszym'),
    (6, 'bezrobotnym'),
]

class Items(models.Model):
    item = models.IntegerField(choices=ITEM_CHOICES)
    bags = models.IntegerField()



class Organization(models.Model):
    name = models.CharField(max_length=255)
    location = models.IntegerField(choices=LOCATION_CHOICES)
    beneficiary = models.IntegerField(choices=BENEFICIARY_CHOICES)

class Order(models.Model):
    items = models.ForeignKey(Items, on_delete=models.CASCADE)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    post_code = models.IntegerField()
    phone = models.IntegerField()
    date = models.DateField()
    hour = models.TimeField()
    info = models.TextField(blank=True)


