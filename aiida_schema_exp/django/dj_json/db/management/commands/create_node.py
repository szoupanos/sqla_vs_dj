from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def clean(self):
        pass

    def handle(self, *args, **kwargs):
        from db.models import DbNode
        from db.models import DbUser
        from db import timezone
        import json

        min = timezone.now().minute
        sec = timezone.now().second
        msec = timezone.now().microsecond

        usr = DbUser.objects.create(email='{}@{}.{}'.format(msec, sec, min))

        print "Creating node"
        my_json = json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])
        DbNode.objects.create(label='my_node', user=usr, jattributes=my_json,
                              jextras=my_json)
        print "Created"

