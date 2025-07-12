from django.db import models

class Phone (models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    description = models.TextField(blank = True)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    image = models.ImageField (upload_to='phones/',blank=True , null=True)

    def __str__(self):
        return self.name
    
class Ambassadores(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    description = models.TextField(blank = True)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    image = models.ImageField(upload_to='ambassadores/',  blank=True , null= True)

    def __str__(self):
        return self.name  
    
    class Meta:
        verbose_name = 'Амбасадоры'  
        verbose_name_plural = 'Амбасадоры'  

class Our_supports(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='our_supports/', blank= True, null=True)

    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'Нас поддерживают'  
        verbose_name_plural = 'нас поддерживают'  




class Tab(models.Model):
    name = models.CharField(max_length=255)
    brand = models.CharField(max_length=100)
    description = models.TextField(blank = True)
    price = models.DecimalField(max_digits=10 , decimal_places=2)
    image = models.ImageField(upload_to='phones/',blank=True , null=True)

    
    
    def __str__(self):
        return self.name
    

    class Meta:
        verbose_name = 'Планшеты'  
        verbose_name_plural = 'Планшеты'  



