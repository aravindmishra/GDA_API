from django.db import models

# Create your models here.

class GroceryDetails(models.Model):
    product_id = models.AutoField(primary_key = True)
    file_id = models.IntegerField(blank=True, null=True)
    product_name = models.CharField(max_length=270, blank=True, null=True)
    brand = models.CharField(max_length=270, blank=True, null=True)
    catogery_id = models.IntegerField(blank=True, null=True)
    price = models.IntegerField(blank=True, null=True)
    available_qty = models.IntegerField(blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
         db_table = "grocery_details"

    def list(catogery_id = 0):
        query = " SELECT gd.product_id, fd.file_name, gd.product_name, gd.brand, cd.catogery, gd.price, gd.available_qty, sm.status FROM grocery_details AS gd INNER JOIN file_details AS fd ON fd.file_id = gd.file_id INNER JOIN catogery_details AS cd ON cd.catogery_id = gd.catogery_id INNER JOIN status_master AS sm ON sm.status_id = gd.status"
        if int(catogery_id) > 0:
            query = query + " WHERE gd.available_qty > 0 AND gd.catogery_id = {}".format(catogery_id)
        query = query + " ORDER BY product_name ASC"
        return GroceryDetails.objects.raw(query)

class CatogeryDetails(models.Model):
    catogery_id = models.AutoField(primary_key = True)
    catogery = models.CharField(max_length=270, blank=True, null=True)
    status = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True,blank=True, null=True)
    updated_by = models.IntegerField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
         db_table = "catogery_details"


class FileDetails(models.Model):
    file_id = models.AutoField(primary_key = True)
    file_name = models.CharField(max_length=370, blank=True, null=True)
    file_path = models.CharField(max_length=670, blank=True, null=True)
    file_size = models.IntegerField(blank=True, null=True)
    created_by = models.IntegerField(blank=True, null=True)
    created_date = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(blank=True, null=True)
    updated_date = models.DateTimeField(blank=True, null=True)

    class Meta:
         db_table = "file_details"