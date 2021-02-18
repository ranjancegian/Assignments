from django.db import models
import jsonfield

class Item(models.Model):
    name = models.CharField(max_length=100, default='mydata')
    json_data = jsonfield.JSONField(null=True, blank=True)

    def __str__(self):
        return self.name
    

    

    
