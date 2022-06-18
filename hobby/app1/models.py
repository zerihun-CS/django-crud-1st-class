from django.db import models


class Hobby(models.Model):
   # hobby_type = {'vrtiual':'virtual'}
   name = models.CharField(max_length=12)
   type  = models.CharField(max_length=12,blank=True)
   
   def __str__(self):
      return f'name:{self.name} type:{self.type}'