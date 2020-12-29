from django.db import models

# id name description ication year longitude latitude area category states region iso

# SITE
# id name description justification    year    longitude    latitude    area     category    country   region  
# pk str  str         str              int     float        float       float    fk          fk        fk         
#

# COUNTRY
# name          iso
# str(unique)   str(pk)

# REGION
# id region
# pk str

# CATEGORY
# id category


# Cultural, Natural, Mixed
class Category(models.Model) :
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Country(models.Model):
    iso = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self) :
        return self.name

class Site(models.Model):
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=5000, null=True)
    justification = models.CharField(max_length=5000, null=True)
    year = models.IntegerField(null=True)
    longitude = models.FloatField(null=True)
    latitude = models.FloatField(null=True)
    area = models.FloatField(null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self) :
        return self.name