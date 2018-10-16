from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def clean(self):
        pass

    def handle(self, *args, **kwargs):
        from db.models import DbNode
        from db import timezone

        import json
        import time

        sec = timezone.now().second
        msec = timezone.now().microsecond

        print "Finding all the nodes and updating them one by one"
        counter = 0
        start_time = time.time()
        for dbn in DbNode.objects.all():
            my_json_attr = json.dumps(
                ['attr', msec + counter, {'bar': ('baz', None,
                                                  sec + counter, 2)}])
            my_json_extra = json.dumps(
                ['extra', msec + counter, {'bar': ('baz', None,
                                                   sec + counter, 2)}])
            dbn.jattributes = my_json_attr
            dbn.jextras = my_json_extra
            dbn.save()
            counter += 1

        end_time = time.time()
        print("Updated the json fields (attributes and extras) "
              "of {} nodes.".format(counter))

        print "Elapsed time --- {} seconds --- ".format(end_time - start_time)
