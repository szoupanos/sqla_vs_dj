from django.core.management.base import BaseCommand


class Command(BaseCommand):
    """
    Update of a specific part of the JSON field.
    """

    def clean(self):
        pass

    def handle(self, *args, **kwargs):
        from db.models import DbNode
        from db import timezone
        from django.db import transaction
        import time

        print "Finding all the nodes and updating them one by one"
        counter = 0
        start_time = time.time()
        with transaction.atomic():
            for dbn in DbNode.objects.all():
                dbn.jextras[2]['bar'][0] = "aaa"
                dbn.save()
                counter += 1

        end_time = time.time()
        print("Updated the json fields (attributes and extras) "
              "of {} nodes.".format(counter))

        print "Elapsed time --- {} seconds --- ".format(end_time - start_time)
