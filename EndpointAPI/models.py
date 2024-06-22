from django.db import models
from django.utils.timezone import now

'''
I prodotti associati agli ordini presentano una relazione molti a molti
'''

class Product (models.Model):
    ID=models.AutoField(auto_created=True, primary_key=True)
    name=models.CharField(name='name', max_length=255,null=False, blank=False)
    price=models.FloatField(name='price',null=False, blank=False)

    def __str__(self):
        return '%s - %.2f'%(self.name,self.price)

class Order (models.Model):
    ID=models.AutoField(auto_created=True, primary_key=True)
    name=models.CharField(name='name',max_length=255,null=False, blank=False)
    description=models.TextField(name='description',null=True, blank=True)
    date=models.DateTimeField(name='date',default=now, blank=True, editable=True )
    products=models.ManyToManyField(Product, null=True,blank=True)

    def __str__(self):
        return '%s - %s'%(self.name,self.date.strftime('%Y-%m-%d %H:%M:%S'))



