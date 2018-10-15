from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def clean(self):
        pass

    def handle(self, *args, **kwargs):
        from db.models import DbNode, DbGroup
        from db.management.commands import DEFAULT_GROUP_NAME

        # Getting the one and only group with that name
        dbgroup = DbGroup.objects.filter(name=DEFAULT_GROUP_NAME).first()

        # Find all nodes and get the pks
        print "Getting all the pks"
        list_pk = list()
        for dbn in DbNode.objects.all():
            list_pk.append(dbn.pk)

        print "Found #{} pks".format(len(list_pk))

        # Add the pks to the group
        print "Adding the pks to the group"
        dbgroup.dbnodes.add(*list_pk)

        print "Done"
