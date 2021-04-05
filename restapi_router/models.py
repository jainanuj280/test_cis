from django.db import models

class RestRouterDetails(models.Model):
    sapId = models.CharField(max_length=18,default=None)
    hostName = models.CharField(null=True,max_length=14,default=None,unique=True)
    loopBack = models.GenericIPAddressField(protocol='IPv4',unique=True)
    type  = models.CharField(null=True,max_length=10,default=None)