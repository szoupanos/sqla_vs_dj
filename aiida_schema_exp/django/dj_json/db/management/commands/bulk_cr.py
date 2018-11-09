from django.core.management.base import BaseCommand
from db.management.commands import (NUMBER_OF_NODES_TO_CREATE,
                                    DEFAULT_USER_EMAIL)


class Command(BaseCommand):
    """
    Simple addition without any optimization (very likely it does a commit
    on every object creation.
    """

    def clean(self):
        pass

    def handle(self, *args, **kwargs):
        from db.models import DbNode
        from db.models import DbUser
        import json
        import time

        usr, usr_res = DbUser.objects.get_or_create(email=DEFAULT_USER_EMAIL)
        if usr_res:
            print "The user with email {} was created".format(
                DEFAULT_USER_EMAIL)
        else:
            print "The user with email {} was already there".format(
                DEFAULT_USER_EMAIL)

        print "Creating nodes & starting measuring time"
        start_time = time.time()

        counter = 0
        for i in range(NUMBER_OF_NODES_TO_CREATE):
            # print "Creating node number {}".format(i)

            my_json_attr = json.dumps(
                ['attr', i, {'bar': ('baz', None, 1.0, 2)}])
            my_json_extra = json.dumps(
                ['extra', i, {'bar': ('baz', None, 1.0, 2)}])

            DbNode.objects.create(label='my_node_{}'.format(i), user=usr,
                                  jattributes=my_json_attr,
                                  jextras=my_json_extra)
            counter += 1

        end_time = time.time()

        print "{} nodes created".format(counter)
        print "Elapsed time --- {} seconds --- ".format(end_time - start_time)
