from django.core.management.base import BaseCommand
from django.db import transaction
from sqla_comp.models import DbNode, DbGroup

import time

OBJECT_NO = 10000

class Command(BaseCommand):

    def clean(self):
        DbNode.objects.all().delete()

    def handle(self, *args, **kwargs):
        # from dj_experiments.try2.mysite.sqla_comp.models import DbNode, DbGroup

        print "Adding data"
        start_total = time.time()

        print "Creating the group and committing it"
        start_gr = time.time()
        gr = DbGroup(name='Python')
        gr.save()
        print "Time elapsed in sec (group creation and commit)", str(
            time.time() - start_gr)

        print "Creating the nodes and committing them"
        start_n = time.time()
        nodes = list()
        with transaction.atomic():
            for i in range(1, OBJECT_NO):
                n = DbNode(title='Snakes {}'.format(i), body='Ssssssss {}'.format(i))
                n.save()
                nodes.append(n)
        print "Time elapsed in sec (node creation and commit)", str(
            time.time() - start_n)

        print "Adding posts one by one to the category and to the session in general"
        with transaction.atomic():
            start = time.time()
            count = 0
            prev_end = start
            for n in nodes:
                gr.dbnodes.add(n)
                count = count + 1
                if count % 100 == 0:
                    curr_end = time.time()
                    print "Counter: {}, Time elapsed in sec: {}, Throughput (time per 1000 nodes): {}".format(
                        count, str(curr_end - start), str(curr_end - prev_end))
                    prev_end = curr_end
        print "Time elapsed in sec", str(time.time() - start)

        print "Time elapsed in sec (total loading procedure)", str(
            time.time() - start_total)

        print "Data added"

        print "DbGroup ====> ", DbGroup.objects.all()
        print "DbNode ====> ", DbNode.objects.count()

        print "Cleaning tables"
        DbGroup.objects.all().delete()
        DbNode.objects.all().delete()
        print "Tables cleaned"

        print "DbGroup ====> ", DbGroup.objects.all()
        print "DbNode ====> ", DbNode.objects.count()

