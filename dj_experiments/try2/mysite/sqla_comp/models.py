import pytz

from django.db import models
from datetime import datetime

utc = pytz.utc

# class Post(models.Model):
#     title = models.CharField(max_length=80, null=False)
#     body = models.TextField(null=False)
#     pub_date = models.DateTimeField(null=False, default=datetime.utcnow().replace(tzinfo=utc))
#
# class Category(models.Model):
#     name = models.CharField(max_length=50, null=False)
#     posts = models.ManyToManyField('Post', related_name='categories')


class DbNode(models.Model):
    title = models.CharField(max_length=80, null=False)
    body = models.TextField(null=False)
    pub_date = models.DateTimeField(null=False, default=datetime.utcnow().replace(tzinfo=utc))

class DbGroup(models.Model):
    name = models.CharField(max_length=50, null=False)
    dbnodes = models.ManyToManyField('DbNode', related_name='dbgroups')
