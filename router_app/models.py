from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import re

def validate_mac(value):
    if not (re.match("[0-9a-f]{2}([-:]?)[0-9a-f]{2}(\\1[0-9a-f]{2}){4}$", value.lower())):
        raise ValidationError(
            _('%(value)s is not an mac Address'),
            params={'value': value},
        )


class RouterDetails(models.Model):
    sapId = models.CharField(max_length=18,default=None)
    hostName = models.CharField(null=True,max_length=14,default=None)
    loopBack = models.GenericIPAddressField(protocol='IPv4')
    macAdd  = models.CharField(null=True,max_length=17,default=None)