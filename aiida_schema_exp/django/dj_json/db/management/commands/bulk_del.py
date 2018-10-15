from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def clean(self):
        pass

    def handle(self, *args, **kwargs):
        from db.models import DbNode, DbUser, DbGroup

        print "Deleting all nodes"
        DbNode.objects.all().delete()
        print "Deleted"

        print "Deleting all users"
        DbUser.objects.all().delete()
        print "Deleted"

        print "Deleting all groups"
        DbGroup.objects.all().delete()
        print "Deleted"
