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

        for i in range(100):
            print i

            my_json_attr = json.dumps(
                ['attr', i, {'bar': ('baz', None, 1.0, 2)}])
            my_json_extra = json.dumps(
                ['extra', i, {'bar': ('baz', None, 1.0, 2)}])

            DbNode.objects.create(label='my_node_{}'.format(i), user=usr,
                                  jattributes=my_json_attr,
                                  jextras=my_json_extra)

        print "Created"

