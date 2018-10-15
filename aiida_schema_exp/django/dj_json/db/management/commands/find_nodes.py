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

        print "Searching for nodes"

        for dbn in DbNode.objects.all():
            print dbn.id, dbn.label, dbn.jattributes, dbn.jextras

        print "Finished search"

