from django.db import models

# Create models here........................................................................

class Substation(models.Model):
    """Represent a substation object"""
    latitude = models.CharField(max_length=255)
    length = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'The Substation was created in the coordinates: {} , {}'.format(self.latitude, self.length)


class Transformator(models.Model):
    """Represent a transformator object"""
    latitude = models.CharField(max_length=255)
    length = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    substation = models.name = models.ForeignKey(Substation,
                                                 on_delete=models.CASCADE)

class Counter(models.Model):
    is_active= models.BooleanField(default=True)
    location= models.CharField(max_length=30)
    transformator= models.ForeignKey(Transformator,
                                                 on_delete=models.CASCADE)
                        
