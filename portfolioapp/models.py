from django.db import models
class Contact(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=40)
    content=models.CharField(max_length=400)
    number=models.CharField(max_length=10)


    def _self_(self):
        return(self.name)
    def _str_(self):
        return(self.name)

# Create your models here.
