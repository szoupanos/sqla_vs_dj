from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def clean(self):
        pass

    def handle(self, *args, **kwargs):
        from db.management.commands import DEFAULT_GROUP_NAME
        from db.models import DbGroup

        print "Searching for nodes in group {}".format(DEFAULT_GROUP_NAME)

        dbnodes = DbGroup.objects.filter(
                name=DEFAULT_GROUP_NAME).first().dbnodes.all()

        print "Found #{} dbnodes".format(len(dbnodes))

        for dbn in dbnodes:
            print dbn.id, dbn.label, dbn.jattributes, dbn.jextras

        print "Finished search"

