import csv  # https://docs.python.org/3/library/csv.html

from unesco.models import Category, Country, Region, Site


def run():
    fhand = open('./unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader) # Advance past the header

    Category.objects.all().delete()
    Country.objects.all().delete()
    Region.objects.all().delete()
    Site.objects.all().delete()

    # Format of CSV:
    # name description justification    year    longitude    latitude    area     category    states    region  iso
    # 0    1           2                3       4            5           6        7           8         9       10
    for row in reader:

        category, created = Category.objects.get_or_create(name=row[7])
        country, created = Country.objects.get_or_create(iso=row[10], name=row[8])
        region, created = Region.objects.get_or_create(name=row[9])

        site = Site(name=row[0], \
                    description=row[1], \
                    justification=row[2], \
                    year=int(row[3]) if len(row[3]) > 0 else None, \
                    longitude=float(row[4]) if len(row[4]) > 0 else None, \
                    latitude=float(row[5]) if len(row[5]) > 0 else None, \
                    area=float(row[6]) if len(row[6]) > 0 else None, \
                    category=category, \
                    country=country, \
                    region=region)

        site.save()