from django.db import models

# Create models here........................................................................
""" The models in this File are the objetcs than respresent the substations, transformators and
    counters."""

class Substation(models.Model):
    """Represent a substation object"""
    codeSubstation = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    latitudeSubstation = models.CharField(max_length=255)
    lengthSubstation = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return 'The Substation was created in the coordinates: {} , {}'.format(
            self.latitudeSubstation,
            self.lengthSubstation)


class Transformator(models.Model):
    """Represent a transformator object"""
    codeTransformator = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    latitudeTransformator = models.CharField(max_length=255)
    lengthTransformator = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    substationTransformator = models.ForeignKey(Substation,
                                                 on_delete=models.CASCADE)

    def __str__(self):
        return 'The Transformator was created in the coordinates: {} , {}'.format(
            self.latitudeTransformator,
            self.lengthTransformator)

class Counter(models.Model):
    """Represent a counter object"""
    codeCounter = models.AutoField(
        auto_created=True,
        primary_key=True,
        serialize=False,
        verbose_name='ID')
    latitudeCounter = models.CharField(max_length=255)
    lengthCounter = models.CharField(max_length=255)
    value = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)
    addressCounter = models.CharField(max_length=255)
    stratum = models.PositiveSmallIntegerField()
   # clientCounter = models.ForeignKey(Client, related_name='counters',
                                       #on_delete=models.CASCADE)
    transformatorCounter = models.ForeignKey(Transformator,
                                      on_delete=models.CASCADE)

    #def __str__(self):
        #return str(self.codeCounter)


class History(models.Model):
    """Modelo para representar el objero history"""
    codeHistory = models.AutoField(
        auto_created=True,
        primary_key=True,
        verbose_name='ID'
        )
    current = models.PositiveIntegerField()
    consumption = models.PositiveIntegerField()
    registryHistory = models.DateField(auto_now_add=True)
    counter = models.ForeignKey(
        Counter, related_name='historys', on_delete=models.CASCADE)
