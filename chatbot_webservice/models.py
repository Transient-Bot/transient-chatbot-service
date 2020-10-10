from django.db import models


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)


class Dependency(models.Model):
    source = models.ForeignKey(Service, related_name='source', on_delete=models.CASCADE)
    target = models.ForeignKey(Service, related_name='target', on_delete=models.CASCADE)
