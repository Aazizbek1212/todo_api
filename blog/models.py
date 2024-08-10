from django.db import models



class Blog(models.Model):
    name = models.CharField(max_length=400)
    description = models.TextField( blank=True, null=True)


class Category(models.Model):
    name = models.CharField(max_length=500)
