from django.db import models

class Products(models.Model):
    name = models.TextField()
    decs = models.TextField()
    batch_number = models.IntegerField()
    in_stock = models.BooleanField()

def create_product(name, decs, batch_number, in_stock):
    products = Products(
        name = name,
        decs = decs,
        batch_number = batch_number,
        in_stock = in_stock
    )
    products.save()
    return products
    


def all_products():
    return Products.objects.all()

def find_product_by_name(name):
    if len(Products.objects.filter(name = name)) == 0:
        return None
    else:
        return Products.objects.get(name = name)

def stock_products():
     return Products.objects.filter(in_stock = True)

def update_product_decs(name, new_decs):
    contact = find_product_by_name(name)
    contact.decs = new_decs
    contact.save()

def delete_product(name):
    return Products.objects.get(name = name).delete()