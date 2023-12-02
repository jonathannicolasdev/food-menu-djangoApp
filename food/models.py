from django.db import models

# Create your models here.
class Item(models.Model):

    def __str__(self):
        return self.item_name
        
    item_name = models.CharField(max_length=200)
    item_desc = models.CharField(max_length=200)
    item_price = models.IntegerField()
    item_image = models.CharField(max_length=500, default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQp8MdrNj1NpuBB2kQuEmLxgqn9y3ZZWiAipWbkfzkLIN2DGTQ6U9A7LFQH_i5a1fYjtJg&usqp=CAU")

