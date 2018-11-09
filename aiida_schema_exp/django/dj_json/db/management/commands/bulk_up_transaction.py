from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Update of objects that happens within a transaction.
    """

    def clean(self):
        pass

    def handle(self, *args, **kwargs):
        from db.models import DbNode
        from db import timezone
        from django.db import transaction

        import json
        import time

        sec = timezone.now().second
        msec = timezone.now().microsecond

        print "Finding all the nodes and updating them one by one"
        counter = 0
        start_time = time.time()
        with transaction.atomic():
            for dbn in DbNode.objects.all():
                my_json_attr = ['attr', msec + counter, {'bar': ('baz', None,
                                                      sec + counter, 2)}]
                my_json_extra = ['extra', msec + counter, {'bar': ('baz', None,
                                                       sec + counter, 2)}]
                dbn.jattributes = my_json_attr
                dbn.jextras = my_json_extra
                dbn.save()
                counter += 1

        end_time = time.time()
        print("Updated the json fields (attributes and extras) "
              "of {} nodes.".format(counter))

        print "Elapsed time --- {} seconds --- ".format(end_time - start_time)
